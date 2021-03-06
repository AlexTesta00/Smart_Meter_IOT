#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alex Testa
"""
import requests, math, time

def get_data_from_IOT():

    # Doc
    """
    Description
    -----------
    Method use to get a real weather data from city,
    to simulate real data for the IOT
    
    Return
    ------
        float
              represent the current temperature (in Celsius)

        int
              represent the current humidty (in percent)
    """
    # API Key used to complete the request for openweathermap.com
    api_key = "9b67791e84d728b1070be77395a687ad"
  
    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
    # The city name
    city_name = "Riccione"
    
    # Complete Url to send a request for openweathermap.com
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
  
    # get method of requests module
    # return response json object
    response = requests.get(complete_url)
  
    # json method of response object 
    # convert json format data into
    # python format data
    x = response.json()
    
    # x variable contain the city information
    # if the city return 404 the resource was not found
    # city is not found
    if x["cod"] != "404":
  
        # store the value of "main"
        # key in variable y
        y = x["main"]
  
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = math.trunc(round(y["temp"] - 273,15)) # Convert temperature in celsius from kelvin
  
        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]

    else:

        print("City Not Found ")

    return current_temperature, current_humidity

def get_current_time_measure():
    """
    Description
    -----------
    Use to get the current time of measure
    
    Return
    ------
    string
            Represent the current time
    """
    return time.strftime('%H:%M:%S', time.localtime())


def store_data(file_name, data):
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
    fout = open(file_name, 'a')
    if fout.write('\n' + data):
        return True
    fout.close()
    return False

def get_current_message_format(ip_address, separator = ' - '):
    """
    Description
    -----------
    Use to incapsulate data in correct packet
    
    Parameters:
        string:
            Represent the ip address of the current iot
        
        string:
            Is use to separate the data
    Return
    ------
    string
            the correctly message to send
    """
    return str(ip_address) + separator + str(get_current_time_measure()) + separator + str(get_data_from_IOT()[0]) + 'C??' + separator + str(get_data_from_IOT()[1]) + '%'

    