# -*- coding: utf-8 -*-
"""
@author: Alex Testa
"""

import socket as sk


def tcp_send_message(server_port_tcp, message):
    
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

def replace_ip_in_string(ip, string):
    string = string.replace(string.split()[0], ip)
    return string