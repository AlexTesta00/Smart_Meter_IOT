# -*- coding: utf-8 -*-
"""
@author: Alex Testa
"""

import socket as sk
import datetime as dt
import time as tm

def replace_ip_in_string(ip, string):
    """
    Description
    -----------
    Use to change the ip in a packet
    
    Parameters:
        string:
            Represent the ip that are overwrite
        
        string:
            Represent the string that have the uncorrect ip
    Return
    ------
    string
            The correct message whit correct ip
    """
    string = string.replace(string.split()[0], ip)
    return string

def print_log_file(path, data):
    """
    Description
    -----------
    Use to store data in file
    
    Parameters:
        string:
            Represent the path of the file
        
        string:
            Represent the data to store in file
    Return
    ------
    boolean
            true if the data are print in file
    """
    fout = open(path, 'a')
    if fout.write('\n' + data):
        return True
    fout.close()
    return False


def tcp_send_message(server_port_tcp, message, path_log_file='GatwayLog/log.txt'):
    """
    Description
    -----------
    Use to send data from gatway to central server
    
    Parameters:
        string:
            Represent the server port to tcp conneciton
        
        string:
            Represent the message that is send to central server
        
        string:
            Represent the path of file log if there are exception
    Return
    ------
    exception
            return exception if the connection failed, or the time is over
    """
    # Use to calculate the total speed for send a tcp packet to Central Server
    t_start = tm.time()
    
    # To create a tcp socket
    tcp_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    
    try:
        # This is used to close socket if central server don't reply.
        tcp_socket.settimeout(10)
        # Use to create a conneciton from gatway to central server
        tcp_socket.connect(('localhost', server_port_tcp))
        # Send message to server
        tcp_socket.send(message.encode('utf8'))
        # Wait a central server response
        response = tcp_socket.recv(server_port_tcp)    
        # Stop the time to measure the speed packet
        t_end = tm.time()
        # Print the data 
        print(' Central Server Response : ' + response.decode('utf8'))
        print(' Speed : %s' % str(t_end - t_start)[0:5] + 'ms') # Take only 2 part of mantissa
        
        # Close connection
        tcp_socket.close()
    except Exception as data:
        # Print faillure message
        print(' fail : ', data)
        print(' failed connection')
        print(' Store data ')
        # Store the data if the conneciton faillure or the time is over
        print_log_file(path_log_file, message + ' Date : ' + str(dt.date.today()))
        # Close connection
        tcp_socket.close()
    
    return
