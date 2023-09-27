from scapy.all import *

# Tabela de Traducao NAT (IP privado -> IP publico)
nat_translation_table = {
    '10.1.1.1': '8.8.254.254',
    '10.1.1.2': '8.8.254.254',  
}

def nat(pkt):
    pkt.show()
    if IP in pkt and pkt[IP].src in nat_translation_table:
        original_src_ip = pkt[IP].src
        translated_src_ip = nat_translation_table[original_src_ip]
        
        # Atualiza o endereco IP de origem
        pkt[IP].src = translated_src_ip
        
        # Encaminha o pacote para a interface de saida apropriada
        if pkt.sniffed_on == 'r-eth1':
            sendp(pkt, iface='r-eth2')
        elif pkt.sniffed_on == 'r-eth2':
            sendp(pkt, iface='r-eth1')
    else:
        return

sniff(iface=["r-eth1", "r-eth2"], filter='ip', prn=nat)
