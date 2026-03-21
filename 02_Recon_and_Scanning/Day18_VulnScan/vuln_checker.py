import socket

print("--- 🛡️ VULNERABILITY CHECKER V1.0 ---")

# Database: Inme se kuch bhi banner mein mila toh warning aayegi
vuln_list = ["OpenSSH_6.6.1", "Apache/2.4.1", "vsFTPd 2.3.4"]

target = input("Enter Target IP: ")
port = int(input("Enter Port: "))

try:
    s = socket.socket()
    s.settimeout(5)
    
    print(f"[*] Connecting to {target}:{port}...")
    s.connect((target, port))
    
    # Banner grab karke decode aur clean karna [cite: 2026-02-06]
    banner = s.recv(1024).decode().strip()
    print(f"\n[*] Found Banner: {banner}")
    
    found = False
    for vuln in vuln_list:
        # Check karna ki kya hamari list ka version banner mein hai [cite: 2026-02-06]
        if vuln in banner:
            print("-" * 50)
            print(f"⚠️  WARNING: Vulnerable version detected! ({vuln})")
            print("👉 Recommendation: Update this service immediately.")
            print("-" * 50)
            found = True
            break
            
    if not found:
        print("\n✅ No known common vulnerabilities found in this banner.")

    s.close()

except Exception as e:
    print(f"\n❌ Error: Could not scan. ({e})")
