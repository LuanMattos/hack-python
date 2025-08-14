#Nesse código vamos fazer um ping falso

from scapy.all import IP, ICMP, send

ip_falso = "10.0.0.99"
ip_alvo = "192.168.1.1"

pkt = IP(src=ip_falso, dst=ip_alvo) / ICMP()
send(pkt)
print(f"Ping falso enviado de {ip_falso} para {ip_alvo}")
