import os
import platform

print("--- NETWORK SWEEPER V1.0 ---")

net = input("Enter Network: ")

print("-"*50)

print("Scanning " + net + ".1 to" + net + ".10..")

print("-"*50)

if platform.system() == "Windown":

    comm = "ping -n 1"
else: 
    comm = "ping -c 1"

for ip in range(1, 11):
    addr = net + "." + str(ip)


    command = comm + " " + addr + " -W 1"

    response = os.system(command)

    if response == 0:
        print(f"Host {addr} is LIVE")
    else:
        print(f"Host {addr} is DOWN")

print("-" * 50)

print("Scan Complete")

