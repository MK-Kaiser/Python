#!/usr/bin/python
import socket
# Create an array of buffers, from 1 to x, with increments of 200.
buffer=["A"]
counter=x
while len(buffer) <= 30:
    buffer.append("A"*counter)
    counter=counter+200
for string in buffer:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Fuzzing PASS with %s bytes" % len(string)
    connect=s.connect(('ip',port))
    s.recv(1024)
    s.send('USER test\r\n')
    s.recv(1024)
    s.send('PASS ' + string + '\r\n')
    s.send('QUIT\r\n')
    s.close()
