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

# def create_server_sender():
#     # Creating a server (host)

#     # Create a socket
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#     # Bind the socket to an IP and port
#     server_socket.bind((HOST, PORT))
#     server_socket.listen(5)

#     print(f"Programmer listening on {HOST}:{PORT}")
#     return server_socket 

def dumper(data_dict):
    return json.dumps(data_dict)

def postman(data):
    return json.loads(data)


reader1_socket = create_client_listen(reader1_ip)
#print(f"Attcker Conneted to Reader1!")

###############################
#   Session 1: shareID, MSG1
###############################

# Receive the messages from the session1: reader1
#BalN
session1_BalN_bin = reader1_socket.recv(1024).decode('utf-8')
reader1_socket.sendall("ok".encode('utf-8'))
print(f"Session1, BalN_bin: {session1_BalN_bin}")
print()

# msg1, session1
session1_msg1_data = postman(reader1_socket.recv(1024).decode('utf-8'))
reader1_socket.sendall("ok".encode('utf-8'))
print("Message 1, Session1, recived.")
print(session1_msg1_data)
print()

session1_PR_bin = session1_msg1_data["PR_bin"]
session1_CHR_hex = session1_msg1_data["CHR_hex"]
session1_TIR_bin = session1_msg1_data["TIR_bin"]

###############################
#     Session 2: ShareID
###############################

reader2_socket = create_client_listen(reader2_ip)
#print(f"Attcker Conneted to Reader2!")

# Receive the messages from the session1: reader1
#BalN
session2_BalN_bin = reader2_socket.recv(1024).decode('utf-8')
reader2_socket.sendall("ok".encode('utf-8'))
print(f"Session2, BalN_bin: {session2_BalN_bin}")
print()

###############################
#      Session 1: MSG2
###############################

#msg2, session1
session1_msg2_data = postman(reader1_socket.recv(1024).decode('utf-8'))
reader1_socket.sendall("ok".encode('utf-8'))
print("Message 2, Session1, recived.")
print(session1_msg2_data)
print()

session1_CHT_hex = session1_msg2_data["CHT_hex"]
session1_AthR_hex = session1_msg2_data["AthR_hex"]
session1_PT_bin = session1_msg2_data["PT_bin"]
session1_TIT_bin = session1_msg2_data["TIT_bin"]

###############################
#      Session 2: MSG1
###############################

# msg1, session2
session2_msg1_data = postman(reader2_socket.recv(1024).decode('utf-8'))
reader2_socket.sendall("ok".encode('utf-8'))
print("Message 1, Session2, recived.")
print(session2_msg1_data)
print()

session2_PR_bin = session2_msg1_data["PR_bin"]
session2_CHR_hex = session2_msg1_data["CHR_hex"]
session2_TIR_bin = session2_msg1_data["TIR_bin"]

###############################
#    Session 1: MSG3, MSG4
###############################

#msg3
session1_msg3_data = postman(reader1_socket.recv(1024).decode('utf-8'))
reader1_socket.sendall("ok".encode('utf-8'))
print("Message 3, Session1, recived.")
print(session1_msg3_data)
print()

session1_PP_bin = session1_msg3_data["PP_bin"]
session1_PQ_bin = session1_msg3_data["PQ_bin"]
session1_Reader_check_hex = session1_msg3_data["Reader_check_hex"]
session1_TIR_prime_bin = session1_msg3_data["TIR_prime_bin"]

#msg4
session1_msg4_data = postman(reader1_socket.recv(1024).decode('utf-8'))
reader1_socket.sendall("ok".encode('utf-8'))
print("Message 4, Session1, recived.")
print(session1_msg4_data)
print()

sesison1_SE_bin = session1_msg4_data["SE_bin"]
sesison1_SF_bin = session1_msg4_data["SF_bin"]
sesison1_SG_hex = session1_msg4_data["SG_hex"]
sesison1_TIS_bin = session1_msg4_data["TIS_bin"]

###############################
#       Session 2: MSG2
###############################

#msg2
session2_msg2_data = postman(reader2_socket.recv(1024).decode('utf-8'))
reader2_socket.sendall("ok".encode('utf-8'))
print("Message 2, Session2, recived.")
print(session2_msg2_data)
print()

session2_CHT_hex = session2_msg2_data["CHT_hex"]
session2_AthR_hex = session2_msg2_data["AthR_hex"]
session2_PT_bin = session2_msg2_data["PT_bin"]
session2_TIT_bin = session2_msg2_data["TIT_bin"]

###############################
#    Session 2: MSG3, MSG4
###############################

#msg3
session2_msg3_data = postman(reader2_socket.recv(1024).decode('utf-8'))
reader2_socket.sendall("ok".encode('utf-8'))
print("Message 3, Session2, recived.")
print(session2_msg3_data)
print()

session2_PP_bin = session2_msg3_data["PP_bin"]
session2_PQ_bin = session2_msg3_data["PQ_bin"]
session2_Reader_check_hex = session2_msg3_data["Reader_check_hex"]
session2_TIR_prime_bin = session2_msg3_data["TIR_prime_bin"]

#msg4
session2_msg4_data = postman(reader2_socket.recv(1024).decode('utf-8'))
reader2_socket.sendall("ok".encode('utf-8'))
print("Message 4, Session1, recived.")
print(session2_msg4_data)
print()

sesison2_SE_bin = session2_msg4_data["SE_bin"]
sesison2_SF_bin = session2_msg4_data["SF_bin"]
sesison2_SG_hex = session2_msg4_data["SG_hex"]
sesison2_TIS_bin = session2_msg4_data["TIS_bin"]

#############################################
#           Applying the attack             #
#############################################

# Functions
import secrets
import hashlib

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

def binary_xor_4bin(bin1, bin2, bin3, bin4):
    # Gets anu amount of binary numbers,
    # (converts them to same lenth if they are not)
    # Calculates XOR of them and then returns it

    int1 = int(bin1, 2)
    int2 = int(bin2, 2)
    int3 = int(bin3, 2)
    int4 = int(bin4, 2)

    # Perform XOR operation
    result_xor_int = int1 ^ int2 ^ int3 ^ int4

    # Convert the result back to a binary string
    result_xor_bin = bin(result_xor_int)[2:]

    return result_xor_bin

def hash_binary(binary_string):
    # Gets a binary number,
    # returns hash of it in hex
    decimal_number = int(binary_string, 2)
    byte_data = decimal_number.to_bytes((decimal_number.bit_length() + 7) // 8, byteorder='big')
    sha1_hash = hashlib.sha1(byte_data).hexdigest()

    sha1_hash = '0x' + sha1_hash
    return sha1_hash

def session_key_extractor(PR_bin, TIR_bin, PT_bin, TIT_bin, TIS_bin, SE_bin, SF_bin, SG_hex, BalN_bin, session):
    # R0 ^ IDNt
    R0_XOR_IDNt_candidates = []

    for shift_amount in range(0, 160):
        R0_XOR_IDNt_body = rotate_left(PR_bin, shift_amount)
        R0_XOR_IDNt_candidates.append(binary_xor(R0_XOR_IDNt_body, TIR_bin))

    # R0 ^ IDNs
    R0_XOR_IDNs_candidates = []

    for shift_amount in range(0, 160):
        R0_XOR_IDNs_body = rotate_left(PT_bin, shift_amount)
        R0_XOR_IDNs_candidates.append(binary_xor(R0_XOR_IDNs_body, TIT_bin))

    S0_candidates = []

    # Get S0 From SE
    for TIS_shift_amount in range(0, 32):
        shifted_TIS_bin = rotate_left(TIS_bin, TIS_shift_amount)
        S0_body = binary_xor(SE_bin, shifted_TIS_bin)

        for shift_amount in range(0, 160):
            candidate = rotate_left(S0_body, shift_amount)
            S0_candidates.append(candidate)

    # Get S0 From SE
    for TIS_shift_amount in range(0, 32):
        shifted_TIS_bin = rotate_left(TIS_bin, TIS_shift_amount)
        S0_body = binary_xor(SF_bin, shifted_TIS_bin)

        for shift_amount in range(0, 160):
            candidate = rotate_left(S0_body, shift_amount)
            S0_candidates.append(candidate)

    unique_S0_candidates = list(set(S0_candidates))

    found_flag = False
    for _, S0 in enumerate(unique_S0_candidates):
        if _ % 100 == 0:
            print(f"{_}/{len(unique_S0_candidates)}")
        for R0_XOR_IDNs in R0_XOR_IDNs_candidates:
            for R0_XOR_IDNt in R0_XOR_IDNt_candidates:
                # pre_TKST = binary_xor(R0_XOR_IDNt, R0_XOR_IDNs, S0, BalN_bin)
                # pre_TKST = binary_xor_4bin_no2(R0_XOR_IDNt, R0_XOR_IDNs, S0, BalN_bin)
                pre_TKST = binary_xor_4bin(R0_XOR_IDNt, R0_XOR_IDNs, S0, BalN_bin)
                TKST_hex = hash_binary(pre_TKST)

                pre_SG = bin(int(TKST_hex, 16))[2:] + S0 + BalN_bin
                maybe_SG_hex = hash_binary(pre_SG)

                if SG_hex == maybe_SG_hex:
                    found_flag = True
                    print(f"{session}:")
                    print(f"\tSG_hex : {maybe_SG_hex}")
                    print(f"\tTKST_hex : {TKST_hex}")
                    break
            if found_flag == True:
                break
        if found_flag == True:
            break


PR_bin = session1_PR_bin
TIR_bin = session1_TIR_bin
PT_bin = session1_PT_bin
TIT_bin = session1_TIT_bin
TIS_bin = sesison1_TIS_bin
SE_bin = sesison1_SE_bin
SF_bin = sesison1_SF_bin
SG_hex = sesison1_SG_hex
BalN = session1_BalN_bin
session_key_extractor(PR_bin, TIR_bin, PT_bin, TIT_bin, TIS_bin, SE_bin, SF_bin, SG_hex, BalN, "Session 1")

PR_bin = session2_PR_bin
TIR_bin = session2_TIR_bin
PT_bin = session2_PT_bin
TIT_bin = session2_TIT_bin
TIS_bin = sesison2_TIS_bin
SE_bin = sesison2_SE_bin
SF_bin = sesison2_SF_bin
SG_hex = sesison2_SG_hex
BalN = session2_BalN_bin
session_key_extractor(PR_bin, TIR_bin, PT_bin, TIT_bin, TIS_bin, SE_bin, SF_bin, SG_hex, BalN, "Session 2")
