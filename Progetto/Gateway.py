#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Testa
"""

import socket as sk
import time as tm

port = 10000 # the number of the server port
buffer_size = 64 # The size of the buffer
okay_message = 'Okay' # Use in the case that the server recive a correct message
failed_message = 'Failed' # Use in the case that the server recive a uncorrect message

# Create UDP socket
UDP_Socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

# Associate the socket whit the server port
server_address = ('localhost', port)
print(' Starting work on : %s \n Port : %s' % server_address)

# Associate the server address whit the sicket
UDP_Socket.bind(server_address)

while True:
    print('\n\r wating data...')
    data, address = UDP_Socket.recvfrom(buffer_size)
    
    #Data reciver
    print(' Recived data...\n Bytes : %s \n Ip_Sender : %s' % (len(data), address))
    print (' Message : ' + data.decode('utf8'))
    
    #Control data
    if data:
        print( ' Dati inviati correttamente')
        send_data = UDP_Socket.sendto(okay_message.encode(), address)
    else:
        print(' Dati non corretti')
        send_data = UDP_Socket.sendto(failed_message.encode(), address)