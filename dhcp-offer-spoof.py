# responder com IP falso em rede

from scapy.all import *

def send_dhcp_offer(mac, yiaddr):
    ether = Ether(src=RandMAC(), dst=mac)
    ip = IP(src="192.168.1.1", dst="255.255.255.255")
    udp = UDP(sport=67, dport=68)
    bootp = BOOTP(op=2, yiaddr=yiaddr, siaddr="192.168.1.1", chaddr=mac2str(mac))
    dhcp = DHCP(options=[("message-type", "offer"),
                        ("server_id", "192.168.1.1"),
                        ("lease_time", 43200),
                        ("subnet_mask", "255.255.255.0"),
                        ("router", "192.168.1.1"),
                        "end"])
    pkt = ether / ip / udp / bootp / dhcp
    sendp(pkt)

# Exemplo de uso
send_dhcp_offer("00:11:22:33:44:55", "192.168.1.150")
