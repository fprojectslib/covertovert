# import scapy
from scapy.all import IP, ICMP, send

# Implement your ICMP sender here
packet = IP(dst = "receiver", ttl = 1) / ICMP()
if __name__ == "__main__":
    send(packet)