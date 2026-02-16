import socket
import sys

print("--- 📡 CYBER PORT SCANNER V2.0 (Multi-Scan) ---")

# 1. Target IP Input
target = input("Enter Target IP (e.g., 8.8.8.8): ")

print("-" * 50)
print(f"Scanning Target: {target}")
print("Checking Ports from 1 to 100...")
print("-" * 50)

try:
    # 2. Loop: 1 se 100 tak ports scan karne ke liye
    for port in range(1, 101):
        # Socket create karna
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Timeout kam rakha hai taaki scan jaldi ho (0.5 second)
        s.settimeout(0.5)
        
        # Connection try karna
        result = s.connect_ex((target, port))
        
        # Agar result 0 hai, matlab port khula hai
        if result == 0:
            print(f"✅ [OPEN] Port {port} is active!")
        
        # Socket band karna zaroori hai loop ke andar
        s.close()

except KeyboardInterrupt:
    print("\nStopping scan...")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()

except socket.error:
    print("\nServer nahi mil raha.")
    sys.exit()

print("-" * 50)
print("Scan Complete! Sabse important ports check ho gaye.")
