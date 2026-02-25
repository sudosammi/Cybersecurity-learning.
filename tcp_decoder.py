import socket
import struct

def start_sniffing():
    sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    print("[*] TCP Decoder Active... Waiting for traffic...")

    while True:
        try:
            raw_data, addr = sniffer.recvfrom(65535)
            
            # Technical Logic: Packet Length Check
            # Ethernet (14) + IP (20) + TCP (20) = Minimum 54 bytes
            if len(raw_data) < 54:
                continue # Agar packet chota hai, toh use chhod do (Skip iteration)
            
            ip_header = raw_data[14:34]
            iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
            src_ip = socket.inet_ntoa(iph[8])
            dest_ip = socket.inet_ntoa(iph[9])

            tcp_header = raw_data[34:54]
            tcph = struct.unpack('!HHLLBBHHH', tcp_header)
            
            src_port = tcph[0]
            dest_port = tcph[1]

            print(f"[+] {src_ip}:{src_port} --> {dest_ip}:{dest_port}")
            
        except KeyboardInterrupt:
            print("\n[X] Stopping...")
            break # User ne Ctrl+C dabaya, toh loop rok do

start_sniffing()
