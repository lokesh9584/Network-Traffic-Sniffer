#!/usr/bin/python3
from scapy.all import rdpcap
import sys

file = sys.argv[1]

# Read the pcap file
packets = rdpcap(file)

ip_count = {}

# Iterate over packets and count IP occurrences
for packet in packets:
    if packet.haslayer('IP'):
        src_ip = packet['IP'].src
        if src_ip in ip_count:
            ip_count[src_ip] += 1
        else:
            ip_count[src_ip] = 1

# Filter and display IPs that have repeated occurrences
for ip, count in ip_count.items():
    if count > 1:  # IP addresses that appear more than once
        print(f"IP: {ip}, Count: {count}")
