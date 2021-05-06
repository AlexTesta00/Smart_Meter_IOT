#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Testa
"""
import IOT_Function as fun
import socket as sk
import time as tm

port = 10000 # The number of the socket port
my_ip = '192.168.1.1' # The local interface ip address
buffer_size = 64 # The size of the buffer for the message

while True:
    
    for steps in range(4):
        
        # Create UDP socket
        UDP_Socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

        # Associate the socket whit the server port
        server_address = ('localhost', port)
        

        # This is message to send, whit diffent ip for different IOT
        message = fun.get_current_message_format(my_ip + str((steps)))

        # Send message
        sent = UDP_Socket.sendto(message.encode(), server_address)

        # Wait server response
        data, server = UDP_Socket.recvfrom(buffer_size)
        
        # This is the server response
        print('IOT ' + str(steps) + ' server response : ' + data.decode('utf8'))
        
        # If the message failed, the data can store in a log file for not lost the data
        if data.decode('utf8') == 'Failed':
            fun.store_data('IOTLog/log.txt', fun.get_current_message_format(my_ip + str((steps))))

        # Close connection
        UDP_Socket.close()
    
        tm.sleep(3)