#!/usr/bin/env python3
import socket

import os

RECV_BUFFER = 4096
current_dir = os.getcwd()

def change_dir(in_data):
    (_,newdir) = str(in_data).split()
    current_dir = newdir
    print ('current_dir = ',current_dir)
    return True

def list_dir():
    print ('In listdir')
    print (os.listdir(current_dir))
    return os.listdir(current_dir)

# Create the socket as a TCP internet socket.
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# This is a helper method that returns the local hostName of computer that we’re running on.
hostname = socket.gethostname() 

# This is the port we will be listening on.
port=8083
# Bind the hostname/port to the the socket object s.
s.bind((hostname,port))
# Listen on the socket.  The supplied parameter is the number of queued requests from clients
# that are allowed before the server refuses to accept new connections.  Note that in 3.5
# this parameter is now optional.
s.listen(5)

# Accept the socket client connection
# c is the data received from the client.  Addr is a list containing, among other things, the 
# IP address of the client that sent the request. 
c,addr = s.accept()
print ('Connection accepted from ' + str(addr[1]))
c.send(bytes('Server connected','utf-8'))

# Loop forever reading and sending to and from the client and doing some processing on it. 
while True: 
    inp = c.recv(RECV_BUFFER)
    inp = inp.decode('UTF-8')
    print ('Got ',str(inp))
    if 'LS' in inp:
        out = list_dir()
        print (str(out))
        c.send(bytes(str(out),'UTF-8'))
    elif 'DIR' in inp:
        if change_dir(inp):
            c.send(bytes('New DIR is ' + current_dir,'UTF-8'))
    elif 'Q' in inp:
        break

# Close the server socket.  Note that in this code snippet, this statement never gets reached.  It's
# a good idea to have some sort of exit value that the server understands and will quit if that value
# is sent by the client.
c.close()
