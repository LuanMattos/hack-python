from scapy.all import IP, TCP, send

ip_alvo = "192.168.1.10"
porta_origem = 12345
porta_destino = 80
seq_num = 1000

pkt = IP(dst=ip_alvo) / TCP(sport=porta_origem, dport=porta_destino, flags="R", seq=seq_num)
send(pkt)
print("Pacote RST enviado para fechar conexão")
