from scapy.all import *

def nat(pkt):
    if IP in pkt:
        # Verifica se o pacote é de saída (do host para o servidor)
        if pkt[IP].src == "10.1.1.1":
            # Altera o IP de origem para o endereço público do NAT
            pkt[IP].src = "8.8.254.254"

    return pkt

def nat_router():
    sniff(iface="r-eth0", prn=lambda x: send(nat(x)), filter="ip")

if __name__ == '__main__':
    nat_router()
