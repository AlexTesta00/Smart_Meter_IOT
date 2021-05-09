#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Testa
"""

import socket as sk
import Gatway_Utilities as gt

port = 10000 # The number of the server port
buffer_size = 64 # The size of the buffer for the message from client
okay_message = 'Okay' # Use in the case that the server recive a correct message
failed_message = 'Failed' # Use in the case that the server recive a uncorrect message
recived_packet = 0 # Count the number of the recive packet
all_data = '' # Store the data recived from client
ip_address_local = '192.168.1.27' # The local interface ip address
ip_address_to_central_server = '10.10.10.2' # This is the interface ip that comunicate whit central server
buffer_size = 256 # The buffer dimension to send data in tcp connection
server_port_tcp = 1100 # The number of the server port to tcp conneciton


# Create UDP socket
UDP_Socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

# Associate the socket whit the server port
server_address = ('localhost', port)
print(' Starting work on : %s \n Port : %s' % server_address)

# Associate the server address whit the socket
UDP_Socket.bind(server_address)

while True:
    # Wat data from client
    print('\n\r Wating data...')
    data, address = UDP_Socket.recvfrom(buffer_size)
    
    # Data reciver
    print(' Recived data...\n Bytes : %s \n Ip_Sender : %s' % (len(data), address))
    print(' Buffer Size : %s' % str(buffer_size))
    print (' Message : ' + data.decode('utf8'))
    
    # Control data
    # If the gateway recive all 4 packet, he send packet to central server
    if data:
        send_data = UDP_Socket.sendto(okay_message.encode(), address)
        
        # Increment the counter of the packets
        recived_packet += 1
        
        # Replace the ip, because gatway can send the message to central server whit different ip interface
        all_data += '\n'+ 'IOT : ' + str(recived_packet) + ' Data : ' + gt.replace_ip_in_string(ip_address_to_central_server, data.decode('utf8'))
        
        # When gatway recive all data, he clear the data cache and init the packet counter
        if recived_packet == 4:
            print(' Send data to central server')
            # This part of code send with tcp connection the packet to central server
            gt.tcp_send_message(server_port_tcp, all_data)
            # And clear the data alredy inviated 
            all_data = ''
            # Clear the counter of the packet alredy inviated
            recived_packet = 0
            
    else:
        print(' Uncorrect data')
        send_data = UDP_Socket.sendto(failed_message.encode(), address)
