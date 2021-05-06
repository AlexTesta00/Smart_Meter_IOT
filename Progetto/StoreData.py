# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:59:04 2021

@author: Alex
"""

def store_data(file_name, data):
    fout = open(file_name, 'w')
    if fout.write(data):
        return True
    fout.close()
    return False