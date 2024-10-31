from scapy.all import sniff, ICMP


# Implement your ICMP receiver here
if __name__ == "__main__":
    sniff(filter="icmp", prn=lambda packet: packet.show() if packet.haslayer(ICMP) and packet[ICMP].type == 8 else None, count = 1)