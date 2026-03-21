import socket

def start_sniffer():

    try: 
        sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
        print("[*] Sniffer started... Waiting for 1 packet...")
 
        raw_data, addr =  sniffer.recvfrom(65535)
        print(f"\n[+] Packet Caaptured from: {addr}")

        print(f"[+] Raw Data (Hex): {raw_data.hex()[:100]}...")

    except PermissionError:
        print("[X] Error: Run this script with 'sudo'!")

    except Exception as e:
        print(f"[X] Technical Error: {e}")

start_sniffer()


