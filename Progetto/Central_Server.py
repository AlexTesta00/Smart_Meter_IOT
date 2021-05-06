# -*- coding: utf-8 -*-
"""
@author: Alex Testa
"""

import socket as sk

# The buffer dimension to recive data
buffer_size = 256

# The number of the server port
server_port = 1100

# Use in the case that the server recive a correct message
okay_message = 'Okay'

# Use in the case that the server recive a uncorrect message
failed_message = 'Failed'

# Create TCP socket
server_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

# Associate the server address whit the socket
server_socket.bind(('localhost', server_port))

# Able the socket to recive connection
server_socket.listen(1)

while True:
    
    print(' Wait Connection...')
    # Wait the connection from client
    connection_socket, addr = server_socket.accept()
    print(' Connected ')
    
    try:
        message = connection_socket.recv(buffer_size)
        if message :
            print(' ' + message.decode('utf8'))
            connection_socket.send(okay_message.encode('utf8'))
            connection_socket.close()
            print(' Close connection')
    except IOError:
        connection_socket.send(failed_message.encode('utf8'))
        connection_socket.close()
        print(' Close connection')
        