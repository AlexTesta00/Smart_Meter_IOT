#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Testa
"""
import IOT_Function as fun
import StoreData as st
import socket as sk
import time as tm

port = 10000
my_ip = '192.168.1.1'
buffer_size = 64

while True:
    
    for steps in range(4):
        
        # Create UDP socket
        UDP_Socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

        # Associate the socket whit the server port
        server_address = ('localhost', port)
        

        # This is message to send
        message = fun.get_current_message_format(my_ip + str((steps)))

        # Send message
        sent = UDP_Socket.sendto(message.encode(), server_address)

        # Wait server response
        data, server = UDP_Socket.recvfrom(buffer_size)
        
        print(data)
        if data.decode('utf8') == 'Failed':
            st.store_data('IOTLog/log.txt', fun.get_current_message_format(my_ip + str((steps))))

        # Close connection
        UDP_Socket.close()
    
        tm.sleep(3)