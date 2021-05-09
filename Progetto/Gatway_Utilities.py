# -*- coding: utf-8 -*-
"""
@author: Alex Testa
"""

import socket as sk
import datetime as dt
import time as tm

def replace_ip_in_string(ip, string):
    string = string.replace(string.split()[0], ip)
    return string

def print_log_file(path, data):
    fout = open(path, 'a')
    if fout.write('\n' + data):
        return True
    fout.close()
    return False


def tcp_send_message(server_port_tcp, message, path_log_file='GatwayLog/log.txt'):
    
    t_start = tm.time()
    
    tcp_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    
    try:
        tcp_socket.settimeout(10)
        tcp_socket.connect(('localhost', server_port_tcp))
        tcp_socket.send(message.encode('utf8'))
        response = tcp_socket.recv(server_port_tcp)    
        t_end = tm.time()
        print(' Central Server Response : ' + response.decode('utf8'))
        print(' Speed : %s' % str(t_end - t_start)[0:4] + 'ms') # Take only 2 part of mantissa
    
        tcp_socket.close()
    except Exception as data:
        print(' fail : ', data)
        print(' failed connection')
        print(' Store data ')
        print_log_file(path_log_file, message + ' Date : ' + str(dt.date.today()))
        tcp_socket.close()
    
    return
