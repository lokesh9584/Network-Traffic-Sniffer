#!/bin/python3
from scapy.all import sniff, wrpcap
import sys

# List to hold captured packets
captured_packets = []

if len(sys.argv) < 5:
    print("Usage: python script.py <output_file> <count> <interface> <filter> [<ip_address>]")
    sys.exit(1)

# Define the function that will process each captured packet
def packet_callback(packet):
    # Store the packet in the list
    captured_packets.append(packet)
    print(packet.summary())  # Print a summary of the packet

# Prompts the user for giving the input
output_file = sys.argv[1]
count = int(sys.argv[2])
interface = sys.argv[3]
filter = sys.argv[4]
ip_address = sys.argv[5] if len(sys.argv) > 5 else None

# Append the IP address to the filter if provided
if ip_address:
    filter = f"{filter} and host {ip_address}"

# Start sniffing packets
sniff(prn=packet_callback, count=count, iface=interface, filter=filter)

# Write the captured packets to a pcap file
wrpcap(output_file, captured_packets)
