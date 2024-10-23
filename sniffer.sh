#!/bin/bash

#To check whether the user provided root previliges or not
if [ $EUID -ne 0 ]; then
	echo "Script not executed with root previliges"
	echo "Execute the script with sudo command"
	exit 1
fi

#Prompts the user for entering the required data
read -p "Enter the name of the output file(in .pcap format):" output_file
read -p "Enter the number of packets to capture:" count
read -p "Enter the interface:" interface
read -p "Enter the filter to apply:" filter
read -p "Enter the IP address:" ip_add

#To create the output file if it doesnot exist
if [ ! -f $output_file ]; then
	touch $output_file
fi

echo ""

echo "Starting the capturing process..."

#Command to execute the python script
sudo python3 sample.py "$output_file" $count "$interface" "$filter" "$ip_add"

echo ""
echo "The output_file is stored at:$output_file"

echo ""
sudo python3 IP.py /Users/lokeshloki/Downloads/tool/$output_file


#Command to display the uid&password
echo ""
sudo bash display.sh $output_file
