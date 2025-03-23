import secrets
import hashlib
import socket
import json
import time

stop_time = 5

##########################################
#           Connetions
##########################################

reader1_ip = "192.168.1.104"
reader2_ip = "192.168.1.105"
attacker_ip = "192.168.1.101"
tag1_ip = "192.168.1.102"
supply_ip = "192.168.1.103"

# HOST = supply_ip
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
#   Session #1: Sharing ID of the nodes
##########################################

# Connecting to reader1
reader1_socket = create_client_listen(reader1_ip)
print("Supply chain Connected to Reader1!")

# Getting ID of Reader1, BalN_bin, BS_bin
ids_reader1_data = postman(reader1_socket.recv(1024).decode('utf-8'))
reader1_socket.sendall("ok".encode('utf-8'))

session1_BalN_bin = ids_reader1_data["BalN_bin"]
session1_BS_bin = ids_reader1_data["BS_bin"]
session1_IDNr_bin = ids_reader1_data["IDNr_bin"]
session1_IDNt_bin = ids_reader1_data["IDNt_bin"]
session1_IDNs_bin = ids_reader1_data["IDNs_bin"]

print(ids_reader1_data)
time.sleep(stop_time-2)

##########################################
#   Session #2: Sharing ID of the nodes
##########################################

# Connecting to reader2
reader2_socket = create_client_listen(reader2_ip)
print("Supply chain Connected to Reader2!")

# Getting ID of Reader1, BalN_bin, BS_bin
ids_reader2_data = postman(reader2_socket.recv(1024).decode('utf-8'))
reader2_socket.sendall("ok".encode('utf-8'))

session2_BalN_bin = ids_reader2_data["BalN_bin"]
session2_BS_bin = ids_reader2_data["BS_bin"]
session2_IDNr_bin = ids_reader2_data["IDNr_bin"]
session2_IDNt_bin = ids_reader2_data["IDNt_bin"]
session2_IDNs_bin = ids_reader2_data["IDNs_bin"]

print(ids_reader2_data)
time.sleep(stop_time)

##########################################
#   Session #1: MSG3, Recieving
##########################################

msg3_data = postman(reader1_socket.recv(1024).decode('utf-8'))
reader1_socket.sendall("ok".encode('utf-8'))

session1_PP_bin = msg3_data["PP_bin"]
session1_PQ_bin = msg3_data["PQ_bin"]
session1_Reader_check_hex = msg3_data["Reader_check_hex"]
session1_TIR_prime_bin = msg3_data["TIR_prime_bin"]

print(f"Recieved: Msg 3, session 1:")
print(msg3_data)
time.sleep(stop_time)

##########################################
#   Session #1: MSG4, Sending
##########################################

# YRS
# IDNs_bin || BS_bin || IDNr_bin (? is this ok ?)
pre_YRS = session1_IDNs_bin + session1_BS_bin + session1_IDNr_bin
YRS_hex = hash_binary(pre_YRS)

session1_TIS_bin = random_binary_generator(32)
S0_bin = random_binary_generator(160)

# SE
# IDNs_bin ^ YRS_hex
SE_left_2_bin = binary_xor(session1_IDNs_bin, bin(int(YRS_hex, 16))[2:])
SE_left_bin = rotate_left(session1_TIS_bin, count_one_elements(SE_left_2_bin))

SE_right_bin = rotate_left(S0_bin, count_one_elements(bin(int(YRS_hex, 16))[2:]))

session1_SE_bin = binary_xor(SE_left_bin, SE_right_bin)

# SF
SF_left_bin = rotate_left(S0_bin, count_one_elements(session1_IDNs_bin))
SF_right_bin = rotate_left(session1_TIS_bin, count_one_elements(bin(int(YRS_hex, 16))[2:]))

session1_SF_bin = binary_xor(SF_left_bin, SF_right_bin)

# IDNt_bin ^ BalN_bin ^ S0_bin ^ IDNs_bin
pre_TKST = binary_xor(session1_IDNt_bin, session1_BalN_bin, S0_bin, session1_IDNs_bin)
session1_TKST_hex = hash_binary(pre_TKST)

pre_SG = bin(int(session1_TKST_hex, 16))[2:] + S0_bin + session1_BalN_bin
session1_SG_hex = hash_binary(pre_SG)

msg4 = {
    "SE_bin" : session1_SE_bin,
    "SF_bin" : session1_SF_bin,
    "SG_hex" : session1_SG_hex,
    "TIS_bin" : session1_TIS_bin
}

msg4_json = dumper(msg4)
reader1_socket.sendall(msg4_json.encode('utf-8'))
ok = reader1_socket.recv(1024).decode('utf-8')

time.sleep(stop_time)

##########################################
#   Session #2: MSG3, Recieving
##########################################

msg3_data = postman(reader2_socket.recv(1024).decode('utf-8'))
reader2_socket.sendall("ok".encode('utf-8'))

session2_PP_bin = msg3_data["PP_bin"]
session2_PQ_bin = msg3_data["PQ_bin"]
session2_Reader_check_hex = msg3_data["Reader_check_hex"]
session2_TIR_prime_bin = msg3_data["TIR_prime_bin"]

print(f"Recieved: Msg 3, session 2:")
print(msg3_data)
time.sleep(stop_time)

##########################################
#   Session #2: MSG4, Sending
##########################################

# YRS
# IDNs_bin || BS_bin || IDNr_bin (? is this ok ?)
pre_YRS = session2_IDNs_bin + session2_BS_bin + session2_IDNr_bin
YRS_hex = hash_binary(pre_YRS)

session2_TIS_bin = random_binary_generator(32)
S0_bin = random_binary_generator(160)
print(f"S0_bin: {S0_bin}")

# SE
# IDNs_bin ^ YRS_hex
SE_left_2_bin = binary_xor(session2_IDNs_bin, bin(int(YRS_hex, 16))[2:])
SE_left_bin = rotate_left(session2_TIS_bin, count_one_elements(SE_left_2_bin))

SE_right_bin = rotate_left(S0_bin, count_one_elements(bin(int(YRS_hex, 16))[2:]))

session2_SE_bin = binary_xor(SE_left_bin, SE_right_bin)

# SF
SF_left_bin = rotate_left(S0_bin, count_one_elements(session2_IDNs_bin))
SF_right_bin = rotate_left(session2_TIS_bin, count_one_elements(bin(int(YRS_hex, 16))[2:]))

session2_SF_bin = binary_xor(SF_left_bin, SF_right_bin)

# IDNt_bin ^ BalN_bin ^ S0_bin ^ IDNs_bin
pre_TKST = binary_xor(session2_IDNt_bin, session2_BalN_bin, S0_bin, session2_IDNs_bin)
session2_TKST_hex = hash_binary(pre_TKST)

pre_SG = bin(int(session2_TKST_hex, 16))[2:] + S0_bin + session2_BalN_bin
session2_SG_hex = hash_binary(pre_SG)

msg4 = {
    "SE_bin" : session2_SE_bin,
    "SF_bin" : session2_SF_bin,
    "SG_hex" : session2_SG_hex,
    "TIS_bin" : session2_TIS_bin
}

msg4_json = dumper(msg4)
reader2_socket.sendall(msg4_json.encode('utf-8'))
ok = reader2_socket.recv(1024).decode('utf-8')

time.sleep(stop_time)
