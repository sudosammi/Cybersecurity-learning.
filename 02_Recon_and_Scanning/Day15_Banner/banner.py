import socket

print("--- 🔍 CYBER BANNER GRABBER V1.0 ---")

target = input("ENTER TARGET IP: ")
port = int(input("ENTER PORT: "))

try:
    s = socket.socket()
    s.settimeout(2)
    
    print(f"[*] Connecting to {target}: {port}...")
    s.connect((target, port))
    
    # Raw data receive karke decode karna
    banner = s.recv(1024).decode().strip()
    
    print("-" * 50)
    print("✅ BANNER FOUND: " + banner)
    print("-" * 50)
    
    s.close()

except Exception as e:
    print(f"Error: Banner nahi mila. (Reason: {e})")
