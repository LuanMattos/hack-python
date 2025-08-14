# O módulo optparse do Python serve para criar interfaces de linha de comando (CLI), ou seja, ele permite que seu script aceite argumentos e opções no terminal, como por exemplo:
# python script.py -i 192.168.0.1 -p 80

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--ip", dest="ip", help="IP alvo")
parser.add_option("-p", "--port", dest="port", type="int", help="Porta alvo")

(options, args) = parser.parse_args()

print("IP:", options.ip)
print("Porta:", options.port)





# ⚠️ Importante:
# 📌 optparse está obsoleto desde o Python 2.7 / 3.2.

# ✅ O módulo moderno recomendado hoje é o argparse, que é mais poderoso e ainda mantido.


import argparse
from scapy.all import ICMP, IP, sr1
import time

# Configurando argumentos da linha de comando
parser = argparse.ArgumentParser(description="Ping simples com Scapy")
parser.add_argument("host", help="IP ou hostname de destino")
parser.add_argument("-c", "--count", type=int, default=4, help="Número de pacotes a enviar (padrão: 4)")
args = parser.parse_args()

# Função de ping
def ping(host, count):
    print(f"Ping em {host} com {count} pacotes:")
    for i in range(count):
        pkt = IP(dst=host)/ICMP()
        start = time.time()
        reply = sr1(pkt, timeout=1, verbose=0)
        end = time.time()

        if reply:
            rtt = (end - start) * 1000
            print(f"{i+1}: Resposta de {reply.src}: tempo={rtt:.2f} ms")
        else:
            print(f"{i+1}: Sem resposta")

# Chamando a função
ping(args.host, args.count)
