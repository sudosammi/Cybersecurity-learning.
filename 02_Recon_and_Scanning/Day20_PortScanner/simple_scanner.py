import socket

target = input("Enter Target IP: ")

print(f"[*] Scanning {target} from Port 1 to 100...")

try:
    for port in range(1, 101):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1) 
        
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"[+] Port {port} is OPEN!")
            
        s.close()

except KeyboardInterrupt:
    print("\n[X] Scan stopped by user.")
except Exception as e:
    print(f"[X] Error: {e}")

print("[*] Scan completed.")
