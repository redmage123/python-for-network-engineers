#!/usr/bin/env python3
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

commands = ('DIR /usr/local/etc','LS','Q')
#try:
s.connect((socket.gethostname(),8083))
#except (socket.error,e):
#    if e.args[0] == errno.ECONNREFUSED:
#        raise SystemExit(“Connection was refused by the server”)
#    else:
#        raise SystemExit(“Unknown socket connection error”)
#finally:
#    if s != None:
print (s.recv(1024))

while True:
    for command in commands:
        print  ('Sending ',command)
        s.send(bytes(command,'utf-8'))
        out = s.recv(2048)
        print (out.decode('UTF-8'))
s.close()
