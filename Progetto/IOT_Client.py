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
measure_time = 3 # This variable simulate (in second) the time that the IOT send data to gateway
log_file_name = 'IOT_Log/log.txt' # This is the file name used to store data when gatway connection failed or 

while True:
    
    for steps in range(4):
        
        try:
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
                fun.store_data(log_file_name, fun.get_current_message_format(my_ip + str((steps))))

        except :
            # If the conneciton to gatway failed, store data in log file
            print('Failed Connection to gatway')
            print('Store data log')
            fun.store_data(log_file_name, fun.get_current_message_format(my_ip + str((steps))))
            UDP_Socket.close()

        # Simulate the measure time
        tm.sleep(measure_time)