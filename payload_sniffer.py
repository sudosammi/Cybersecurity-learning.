import socket
import struct

def start_sniffing():
    sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    print("[*] Payload Sniffer Active... Waiting for data...")

    while True:
        try:
            raw_data, addr = sniffer.recvfrom(65535)
            
            # Minimum length check (Filtering out noise)
            if len(raw_data) < 54:
                continue
                
            # IP Header
            ip_header = raw_data[14:34]
            iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
            src_ip = socket.inet_ntoa(iph[8])
            dest_ip = socket.inet_ntoa(iph[9])

            # TCP Header
            tcp_header = raw_data[34:54]
            tcph = struct.unpack('!HHLLBBHHH', tcp_header)
            src_port = tcph[0]
            dest_port = tcph[1]

            # NEW: Payload Extraction (Layer 7)
            # 54 bytes ke baad jo bhi hai, wo actual data hai
            raw_payload = raw_data[54:]
            
            # Decoding binary into readable text
            # 'ignore' errors taaki script crash na ho agar data encrypted ho
            readable_payload = raw_payload.decode('utf-8', errors='ignore')

            # Agar payload mein kuch likha hai, tabhi print karo
            if len(readable_payload) > 0:
                print(f"\n[+] Connection: {src_ip}:{src_port} --> {dest_ip}:{dest_port}")
                print(f"[*] Payload Data: {readable_payload[:100]}...") # Sirf shuruat ke 100 characters print karega
            
        except KeyboardInterrupt:
            print("\n[X] Stopping Sniffer...")
            break

start_sniffing()
