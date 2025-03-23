import secrets
import hashlib
import socket
import json
import time

##########################################
#           Connetions
##########################################

reader1_ip = "192.168.1.104"
attacker_ip = "192.168.1.101"
tag1_ip = "192.168.1.102"
supply_ip = "192.168.1.103"
reader2_ip = "192.168.1.105"

PORT = 8713

def create_client_listen(host):
    # Creates connection to the server (host)

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, PORT))

    return client_socket

def dumper(data_dict):
    return json.dumps(data_dict)

def postman(data):
    return json.loads(data)


###############################
#     Session 2: ShareID
###############################

reader2_socket = create_client_listen(reader2_ip)
#print(f"Attcker Conneted to Reader2!")

# Receive the messages from the session1: reader1
#BalN
time.sleep(3)
session2_BalN_bin = reader2_socket.recv(1024).decode('utf-8')
reader2_socket.sendall("ok".encode('utf-8'))
print(f"Session1, BalN_bin: {session2_BalN_bin}")
print()


###############################
#      Session 2: MSG1
###############################

# msg1, session2
session2_msg1_data = postman(reader2_socket.recv(1024).decode('utf-8'))
reader2_socket.sendall("ok".encode('utf-8'))

time.sleep(3)
print("Message 1, Session2, recived.")
print(session2_msg1_data)
print()

session2_PR_bin = session2_msg1_data["PR_bin"]
session2_CHR_hex = session2_msg1_data["CHR_hex"]
session2_TIR_bin = session2_msg1_data["TIR_bin"]

###############################
#  Sending random values for intrupting attacker1
###############################

import random
import string

def random_string(length):
    # Choose from lowercase, uppercase, digits, and punctuation
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

# Generate a random string of length 200
random_msg = random_string(200)
print("Sending Random msg:")
print(random_msg)

time.sleep(3)
reader2_socket.sendall(random_msg.encode('utf-8'))
