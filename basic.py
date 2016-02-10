#!/usr/bin/env python2

import socket
import sys
import os

def mkhttpreq(path, method, host, query):
    return method + " " + path + " HTTP/1.1\r\n" +\
        "Host: " + host + "\r\n" +\
        "Content-Length: " + len(query) + "\r\n" +\
        "\r\n" +\
        query

host = "http://census.daybreakgames.com"
port = 80
api = "/get/ps2:v2/character/"
params = "?character id=5428018587875812257&c:show=name"

c = raw_input("host: " + host + "\nport: " + str(port) + "\napi: " + api + "\nparams: " + params + "\ncorrect? (y/*)")
if(c != "y" and c != "Y"):
    exit(0)

ip = socket.gethostbyname(host)
print("using ip address: " + str(ip))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, int(port)))
s.sendall(mkhttpreq(api, "GET", host, params))

print(s.recv(100000))
