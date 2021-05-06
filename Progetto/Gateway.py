#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Testa
"""

import socket as sk
import time as tm

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


def tcp_send_message(message):
    
    tcp_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    
    try:
        tcp_socket.connect(('localhost', server_port_tcp))
    except Exception as data:
        print(' fail : ', data)
        print(' failed connection')
        tcp_socket.close()
    
    tcp_socket.send(message.encode('utf8'))
    response = tcp_socket.recv(server_port_tcp)    
    print(' Central Server Response : ' + response.decode('utf8'))
    
    tcp_socket.close()
    return

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
    print (' Message : ' + data.decode('utf8'))
    
    # Control data
    # If the gateway recive all 4 packet, he send packet to central server
    if data:
        print( ' Dati inviati correttamente')
        send_data = UDP_Socket.sendto(okay_message.encode(), address)
        
        # When gatway recive all data, he clear the data cache and init the packet counter
        if recived_packet == 4:
            recived_packet = 0
            print(' Invio i dati al server tcp')
            tcp_send_message(all_data)
            all_data = ''
        else:
            all_data += '\n'+ 'IOT : ' + str(recived_packet) + ' Data : ' + data.decode('utf8')
            recived_packet += 1
            
    else:
        print(' Dati non corretti')
        send_data = UDP_Socket.sendto(failed_message.encode(), address)
