#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Testa
"""
import IOT_Function as fun
import socket as sk
import time as tm
import datetime as dt # Use to store the current date if the connection failed
import termcolor as colors # Module used to change text color in terminal

port = 10000 # The number of the socket port
my_ip = '192.168.1.1' # The local interface ip address
buffer_size = 64 # The size of the buffer for the message
measure_time = 3 # This variable simulate (in second) the time that the IOT send data to gateway
log_file_name = 'IOT_Log/log.txt' # This is the file name used to store data when gatway connection failed
connecition_failed_error = colors.colored('Failed Conneciton', 'red') # The message to user that coumincate an error gatway
online_iot_text = colors.colored('IOT System Online', 'green') # Used to comunicate to user that the system is online
offline_iot_text = colors.colored('IOT system offline :(', 'red') # Used to comunicate that the IOT system is offline

# Used to comunicate whit user that the system is online
print(online_iot_text)

while True:

    for steps in range(4):
        
        try:
            
            # Use to calculate the total speed for send a udp packet to Gatway
            t_start = tm.time()
            
            # Create UDP socket
            UDP_Socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
            
            # Associate the socket whit the server port
            server_address = ('localhost', port)
            
            # This is message to send, whit diffent ip for different IOT
            message = fun.get_current_message_format(my_ip + str((steps)))
            
            # Send message
            sent = UDP_Socket.sendto(message.encode(), server_address)
            
            
            # This is used to close socket if gateway don't reply. 
            UDP_Socket.settimeout(10)

            # Wait server response
            data, server = UDP_Socket.recvfrom(buffer_size)
            
            # Use to calculate the total speed for send a udp packet to Gatway
            t_end = tm.time()
            
            # This is the server response
            print('IOT ' + str(steps) + ' server response : ' + data.decode('utf8'))
            
            # Calculate the total speed for send a udp packet to Gatway from IOT
            print('Speed : %s' % str(t_end - t_start)[0:5] + 'ms') # Take only 2 part of mantissa
    
            # If the message failed, the data can store in a log file for not lost the data
            if data.decode('utf8') == 'Failed':
                # Print data in log file
                fun.store_data(log_file_name, fun.get_current_message_format(my_ip + str((steps))) + ' Date : ' + str(dt.date.today())) # Append the current date

        except :
            # If the conneciton to gatway failed, store data in log file
            print(connecition_failed_error)
            print('Store data log....')
            # If the message failed, the data can store in a log file for not lost the data
            fun.store_data(log_file_name, fun.get_current_message_format(my_ip + str((steps))) + ' Date : ' + str(dt.date.today())) # Append the current date
            # Close socket
            UDP_Socket.close()

        # Simulate the measure time
        tm.sleep(measure_time)

# Used to comunicate whit user that the system is offline
print(offline_iot_text)