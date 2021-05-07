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
    
    print('\nWait Connection...')
    # Wait the connection from client
    connection_socket, addr = server_socket.accept()
    
    # The Client was connected
    print('Connected')
    print('\n')
    
    # Try to recive data
    try:
        message = connection_socket.recv(buffer_size)
        
        # If message have long > 0, take data, store it, and send reponse to clinet
        if message :
            print('Recived Data from : %s \n%s \nBytes : %s' % (addr, message.decode('utf8'), len(message)))
            # Send the reponse to client
            connection_socket.send(okay_message.encode('utf8'))
            # Close connection
            connection_socket.close()
            print('Close connection')
    except IOError:
        # If the data are compromised, send faillure to client and close connection
        connection_socket.send(failed_message.encode('utf8'))
        connection_socket.close()
        print('Close connection')
        