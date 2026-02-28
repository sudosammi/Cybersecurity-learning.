# Technical Syntax: Using Scapy for ARP Packets
import scapy.all as scapy

def scan(ip):
    # 1. Create ARP Request (Teacher's question)
    arp_request = scapy.ARP(pdst=ip)
    
    # 2. Create Ethernet Broadcast (Chilana in class)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # 3. Combine them
    arp_request_broadcast = broadcast/arp_request
    
    # 4. Send and Receive (Getting the Roll Number)
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)

# Scanning your local network range (Check your IP with ifconfig first)
scan("10.0.2.1/24")
