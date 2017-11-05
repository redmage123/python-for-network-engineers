#!/usr/bin/env python
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hostname = socket.gethostname()
port=8083

s.bind(hostname,port)
s.listen(5)

while True:
    c.addr = s.accept()
    print ('Connection accepted from ' + str(addr[1]))
    c.send('Server connected') 
    print (c.recv(1024))
