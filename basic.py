#!/usr/bin/env python2

import socket
import sys
import os

#a function for building HTTP requests
def mkhttpreq(path, method, host, query):
    return method + " " + path + " HTTP/1.1\r\n" +\
        "Host: " + host + "\r\n" +\
        "Content-Length: " + str(len(query)) + "\r\n" +\
        "\r\n" +\
        query

#information about the server and the path there we access
host = "census.daybreakgames.com"
port = 80
api = "/get/ps2:v2/character/"
#our arguments to the web application
params = "?character id=5428018587875812257&c:show=name"

#confirm this information with user
c = raw_input("host: " + host + "\nport: " + str(port) + "\napi: " + api + "\nparams: " + params + "\ncorrect? (y/*)")
if(c != "y" and c != "Y"):
    exit(0)

#get the IP address of the server
ip = socket.gethostbyname(host)
print("using ip address: " + str(ip))

#open a socket and connect it to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

#send our HTTP request
s.sendall(mkhttpreq(api, "GET", host, params))

#receive the HTTP header (up to 100000 chars)
print(s.recv(100000))
#receive the HTTP body (up to 100000 chars)
print(s.recv(100000))
