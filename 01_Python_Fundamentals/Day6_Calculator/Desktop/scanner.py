import socket  # Step A: Socket library mangwao (Phone lagane ki machine)

# Step B: Kisko call karna hai? (Target)
target_ip = input("Enter Target IP: ")  # User se pucho kis IP ko scan karna hai

# Step C: Port 1 se 100 tak check karenge (Jaise ghar ke 100 darwaze check karna)
# range(1, 100) ka matlab port 1 se shuru karo aur 99 tak jao
print("Scanning shuru ho rahi hai...")

for port in range(1, 100):
    # Step D: Socket banao (Phone uthao)
    # AF_INET = IPv4 (Naya pata type)
    # SOCK_STREAM = TCP (Reliable connection, bhagne wala nahi)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Step E: Timeout set karo (Agar 0.5 second mein darwaza na khule, toh aage badho)
    s.settimeout(0.5)
    
    # Step F: Ghanti bajao (Connect karne ki koshish)
    # connect_ex 0 return karta hai agar connection successful ho (Darwaza khula hai)
    result = s.connect_ex((target_ip, port))
    
    if result == 0:
        print(f"[+] Port {port} Khula hai! (OPEN)")
        
    s.close() # Step G: Phone rakh do (Connection band)

print("Scanning khatam!")
