import os 

import socket

print("---THE BANNER HUNTER V1.0---")

print("Targeting Network & Scanning ports Automatically")

print("-" * 50)

net = input("Enter Network:" )

important_ports = [21, 22, 53, 80, 443]

print(f"\n[*] Starting Hunt on Network: {net}.X")
print("-" * 50)

for i in range(1,16):
    ip = net + "-" + str(i)
   
    ping_cmd = "ping -c 1 -W 1 " + ip + ">/dev/null 2>&1"

    response = os.system(ping_cmd)

    if response == 0:

        print(f"\n[+] HOST LIVE: {ip}")
        print("    Scanning important ports...")

        for port in important_ports:

            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(0.5)
            
            result = s.connect_ex((ip, port))
            if result == 0:
               print(f"      PORT {port} is OPEN!!")


            s.close()


print("-" * 50)

print("HUNT Complete!!!")

