import secrets
import hashlib
import socket
import json
import time

stop_time = 5

##########################################
#          Session1: Connetions
##########################################

reader1_ip = "192.168.1.104"
attacker_ip = "192.168.1.101"
tag1_ip = "192.168.1.102"
supply_ip = "192.168.1.103"

# HOST = "192.168.1.100"
PORT = 8713

def create_client_listen(host):
    # Creates connection to the server (host)

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, PORT))

    return client_socket

def create_server_sender():
    # Creating a server (host)

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to an IP and port
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"Programmer listening on {HOST}:{PORT}")
    return server_socket 

def dumper(data_dict):
    return json.dumps(data_dict)

def postman(data):
    return json.loads(data)

# Connection to reader1
reader1_socket = create_client_listen(reader1_ip)
print(f"Tag1 Conneted to Reader1!")

##########################################
#           functions
##########################################

def random_binary_generator(n):
    # Gets integer n,
    # Generates n random bits and returns it 
    # (Without the 0b)
    random_bits = secrets.randbits(n)
    binary_string = bin(random_bits)[2:]
    binary_string = binary_string.zfill(n)

    return binary_string

def count_one_elements(binary_number):
    # Gets a binary number,
    # Counts '1' elements in binary number and returns it
    count = 0
    for digit in binary_number:
        if digit == '1':
            count += 1
    return count

def rotate_left(binary_number, shift_amount):
    # Gets a binary number and shitf amount,
    # Returns rotated number in binary
    rotated_binary = binary_number[shift_amount:] + binary_number[:shift_amount]
    return rotated_binary

def rotate_right(binary_number, shift_amount):
    # Gets a binary number and shitf amount,
    # Returns rotated number in binary
    rotated_binary = binary_number[-shift_amount:] + binary_number[:-shift_amount]
    return rotated_binary

def binary_xor(*args):
    # Gets anu amount of binary numbers, 
    # (converts them to same lenth if they are not)
    # Calculates XOR of them and then returns it

    max_length = max(len(binary_string) for binary_string in args)
    padded_args = [binary_string.zfill(max_length) for binary_string in args]
    xor_binary_string = ''.join(str(sum(int(bit) for bit in bits) % 2) for bits in zip(*padded_args))

    return xor_binary_string

def hash_binary(binary_string):
    # Gets a binary number,
    # returns hash of it in hex
    decimal_number = int(binary_string, 2)
    byte_data = decimal_number.to_bytes((decimal_number.bit_length() + 7) // 8, byteorder='big')
    sha1_hash = hashlib.sha1(byte_data).hexdigest()

    sha1_hash = '0x' + sha1_hash
    return sha1_hash


##########################################
#        Sharing ID of the nodes
##########################################

# Getting ID of Reader1, BalN_bin, BS_bin
ids_reader1_data = postman(reader1_socket.recv(1024).decode('utf-8'))
reader1_socket.sendall("ok".encode('utf-8'))

BalN_bin = ids_reader1_data["BalN_bin"]
BS_bin = ids_reader1_data["BS_bin"]
IDNr_bin = ids_reader1_data["IDNr_bin"]
IDNt_bin = ids_reader1_data["IDNt_bin"]
IDNs_bin = ids_reader1_data["IDNs_bin"]

print(ids_reader1_data)
time.sleep(stop_time)

##########################################
#    Session1: MSG1, Recieving
##########################################

# msg1
msg1_data = postman(reader1_socket.recv(1024).decode('utf-8'))
reader1_socket.sendall("ok".encode('utf-8'))
print("Session1, Message 1 recieved.")
print(msg1_data)
print()

PR_bin = msg1_data["PR_bin"]
CHR_hex = msg1_data["CHR_hex"]
TIR_bin = msg1_data["TIR_bin"]

time.sleep(stop_time)

##########################################
#    Session1: MSG2, Sending
##########################################

TIT_bin = random_binary_generator(32)

# Extract R0
# IDNt_bin ^ TIR_bin
shift_amount_bin = binary_xor(IDNt_bin, TIR_bin)
shifted_number_bin = rotate_right(PR_bin, count_one_elements(shift_amount_bin))

# shifted_number_bin ^ IDNt_bin ^ TIR_bin
R0_bin = binary_xor(shifted_number_bin, IDNt_bin, TIR_bin)

# CHT
# R0_bin ^ IDNt_bin ^ BalN_bin
pre_CHT_bin = binary_xor(R0_bin, IDNt_bin, BalN_bin)
CHT_hex = hash_binary(pre_CHT_bin)

# PT
# R0_bin ^ IDNs_bin ^ TIT_bin
PT_1_bin = binary_xor(R0_bin, IDNs_bin, TIT_bin)

# TIT_bin ^ IDNt_bin
PT_2_bin = binary_xor(TIT_bin, IDNt_bin)

PT_bin = rotate_left(PT_1_bin ,count_one_elements(PT_2_bin))

# AthR
# CHT_hex ^ R0_bin ^ PT_bin ^ IDNt_bin ^ TIT
pre_AthR = binary_xor(bin(int(CHT_hex, 16))[2:], R0_bin, PT_bin, IDNt_bin, TIT_bin)
AthR_hex = hash_binary(pre_AthR)

msg2 = {
    "CHT_hex": CHT_hex,
    "AthR_hex": AthR_hex,
    "PT_bin": PT_bin,
    "TIT_bin": TIT_bin
}

msg2_json = dumper(msg2)
reader1_socket.sendall(msg2_json.encode('utf-8'))
ok = reader1_socket.recv(1024).decode('utf-8')
print(f"Msg2, session 1: {msg2}")

time.sleep(stop_time)
