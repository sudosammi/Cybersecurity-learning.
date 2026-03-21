import socket
import struct

def start_decoder():
    # Technical English: Creating a Raw Socket
    sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    print("[*] Decoder active... Waiting for network traffic...")

    while True:
        raw_data, addr = sniffer.recvfrom(65535)
        
        # Technical Logic: The IP Header starts after 14 bytes of Ethernet Header
        ip_header = raw_data[14:34]
        
        # Unpacking the binary data (Technical Syntax)
        # '!BBHLL' is the format for IP Header parts
        iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
        
        # Extracting Source and Destination IP
        src_ip = socket.inet_ntoa(iph[8])
        dest_ip = socket.inet_ntoa(iph[9])
        
        print(f"[+] Source: {src_ip} | Destination: {dest_ip}")

try:
    start_decoder()
except KeyboardInterrupt:
    print("\n[X] Stopping Decoder...")
