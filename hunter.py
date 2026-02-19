import os
import socket

print("--- 🦅 THE BANNER HUNTER V1.0 ---")
print("Targeting Network & Scanning Ports Automatically")
print("-" * 50)

# User se network ka pehla hissa lo
net = input("Enter Network (e.g. 10.0.2): ")

# Hum sirf sabse important hacking ports check karenge time bachane ke liye
important_ports = [21, 22, 53, 80, 443]

print(f"\n[*] Starting Hunt on Network: {net}.x")
print("-" * 50)

# 1 se 15 tak IPs check karenge
for i in range(1, 16):
    ip = net + "." + str(i)
    
    # Kal jo command tumhari kaam aayi thi (-W 1 for 1 second wait)
    ping_cmd = "ping -c 1 -W 1 " + ip + " > /dev/null 2>&1"
    
    # 1. Pehle PING karke check karo (Is the host LIVE?)
    response = os.system(ping_cmd)
    
    if response == 0:
        print(f"\n[+] HOST LIVE: {ip}")
        print("    Scanning important ports...")
        
        # 2. Agar host LIVE hai, toh uske Ports check karo (Is the port OPEN?)
        for port in important_ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"    ✅ PORT {port} is OPEN!")
            
            s.close()

print("-" * 50)
print("Hunt Complete! 🦅")
