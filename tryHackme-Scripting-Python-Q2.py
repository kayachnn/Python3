#!/usr/bin/env python3

import sys
import socket
import requests
from bs4 import BeautifulSoup


host = "10.10.86.149"
port = 3010
data = ""

result = 0
operation = ""
number = 0
next_port = 0
initial_url = 'http://'+host + ':'+str(port)

def initial_request(url, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("socket created")
        s.connect((host, port))
        print("connected to the server on port "+ str(port))
        response = requests.get(url)
        if response:
            html = BeautifulSoup(response.text, 'html.parser')
            for a in html.select('a'):
                if a['id'] == 'onPort':
                    print("next port is "+ a.text)
        s.close()
        return int(a.text)
    except socket.error as err:
        print("socket creation failed")


    #make the initial request  to the web server on port 3010
next_port = initial_request(initial_url,port)


    #next request to do the operation
while (next_port != 9765):
    # create a socket for the next port
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("socket created")
        #try to connect to server on the port
        try:
            s.connect((host, next_port))
            print("connected to the server on port "+ str(next_port))
            print("will make the request to the server on port" + str(next_port))
            url = 'http://' + host+ ':' + str(next_port)
            # receive the response and assing the the operation, number, next_port
            response = requests.get(url)
            if response:
                operation = str(response.text.split()[0])
                number = float(response.text.split()[1])
                next_port = int(response.text.split()[2])
                print("operation is " + operation)
                print("number is " + str(number))
                print("next_port is "+ str(next_port))
                if operation == 'add':
                    result += number
                elif operation == 'minus':
                    result -= number
                elif operation == 'divide':
                    result /= number
                elif operation == 'multiply':
                    result *= number
            else:
                print("did not get any result")
        except ConnectionRefusedError as err:
            print("cannot connect on port " + str(next_port))
            #print("will try to make the initial request again")
            #next_port = initial_request(initial_url, port)
            print("will make the request again")
        s.close()
    except socket.error as err:
        print("socket creation failed" + err)
        sys.exit()


print(result)
