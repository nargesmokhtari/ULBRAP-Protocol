import secrets
import hashlib
import socket
import json
import time

stop_time = 5

##########################################
#           Connetions
##########################################

reader2_ip = "192.168.1.105"
attacker_ip = "192.168.1.101"
tag2_ip = "192.168.1.106"
supply_ip = "192.168.1.103"

HOST = reader2_ip
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


reader2_socket = create_server_sender()

# Order of connecting
supply_socket, supply_address = reader2_socket.accept()
print(f"supply: \t {supply_address}")

attacker_socket, attacker_address = reader2_socket.accept()
print(f"attacker: \t {attacker_address}")

tag2_socket, tag2_address = reader2_socket.accept()
print(f"tag2: \t {tag2_address}")

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
#    Session2: Sharing ID of the nodes
##########################################

BalN_bin = random_binary_generator(160)
BS_bin = random_binary_generator(160)
IDNt_bin = random_binary_generator(160)
IDNr_bin = random_binary_generator(160)
IDNs_bin = random_binary_generator(160)

ids_reader2 = {
    "BalN_bin" : BalN_bin,
    "BS_bin": BS_bin,
    "IDNr_bin": IDNr_bin,
    "IDNt_bin": IDNt_bin,
    "IDNs_bin": IDNs_bin
}

ids_reader2_json = dumper(ids_reader2)
tag2_socket.sendall(ids_reader2_json.encode('utf-8'))
supply_socket.sendall(ids_reader2_json.encode('utf-8'))
attacker_socket.sendall(str(BalN_bin).encode('utf-8'))

ok = tag2_socket.recv(1024).decode('utf-8')
ok = supply_socket.recv(1024).decode('utf-8')
ok = attacker_socket.recv(1024).decode('utf-8')

print(ids_reader2)
time.sleep(stop_time)

##########################################
#    Session2: MSG1, Sending
##########################################

R0_bin = random_binary_generator(160)
TIR_bin = random_binary_generator(32)

# PR
# R0_bin ^ IDNt_bin ^ TIR_bin
PR_1_bin = binary_xor(R0_bin, IDNt_bin, TIR_bin)

# TIR_bin ^ IDNt_bin
PR_2_bin = binary_xor(TIR_bin, IDNt_bin)

PR_bin = rotate_left(PR_1_bin ,count_one_elements(PR_2_bin))

# PR_bin ^ IDNt_bin ^ TIR_bin
pre_CHR_bin = binary_xor(PR_bin, IDNt_bin, TIR_bin)
CHR_hex = hash_binary(pre_CHR_bin)

msg1 = {
    "PR_bin": PR_bin,
    "CHR_hex": CHR_hex,
    "TIR_bin": TIR_bin
}

msg1_json = dumper(msg1)
tag2_socket.sendall(msg1_json.encode('utf-8'))
attacker_socket.sendall(msg1_json.encode('utf-8'))

# time.sleep(0.5)
ok = attacker_socket.recv(1024).decode('utf-8')
# ok = tag2_socket.recv(1024).decode('utf-8')

print(f"Sent: Msg 1, session 2:")
print(msg1)
time.sleep(stop_time+3)

##########################################
#    Session2: MSG2, Recieving
##########################################

# msg2
temp = tag2_socket.recv(1024).decode('utf-8')
print(temp)
msg2_data = postman(temp)
attacker_socket.sendall(dumper(msg2_data).encode('utf-8'))
ok = attacker_socket.recv(1024).decode('utf-8')

print(f"Recieved: Msg 2, session 1:")
print(msg2_data)
print()

CHT_hex = msg2_data["CHT_hex"]
AthR_hex = msg2_data["AthR_hex"]
PT_bin = msg2_data["PT_bin"]
TIT_bin = msg2_data["TIT_bin"]
time.sleep(stop_time)

##########################################
#    Session2: MSG3, Sending
##########################################

TIR_prime_bin = random_binary_generator(32)
RC_bin = random_binary_generator(160)
Rd_bin = random_binary_generator(160)

# PP
# TIR_prime_bin ^ IDNs_bin ^ Rd_bin
PP_bin = binary_xor(TIR_prime_bin, IDNs_bin, Rd_bin)

# YRS
# IDNs_bin || BS_bin || IDNr_bin
pre_YRS = IDNs_bin + BS_bin + IDNr_bin
YRS_hex = hash_binary(pre_YRS)

# PQ
PQ_bin = binary_xor(bin(int(YRS_hex, 16))[2:], Rd_bin)

conct_for_reader_ckeck = Rd_bin + TIR_prime_bin
pre_Reader_check = binary_xor(RC_bin, IDNs_bin, BalN_bin, conct_for_reader_ckeck)
Reader_check_hex = hash_binary(pre_Reader_check)

msg3 = {
    "PP_bin" : PP_bin,
    "PQ_bin" : PQ_bin,
    "Reader_check_hex" : Reader_check_hex,
    "TIR_prime_bin" : TIR_prime_bin
}

msg3_json = dumper(msg3)
supply_socket.sendall(msg3_json.encode('utf-8'))
attacker_socket.sendall(msg3_json.encode('utf-8'))

ok = supply_socket.recv(1024).decode('utf-8')
ok = attacker_socket.recv(1024).decode('utf-8')

print(f"Sent: Msg 3, session 2:")
print(msg3)
time.sleep(stop_time)

##########################################
#    Session1: MSG4, Receiving
##########################################

# msg4
msg4_data = postman(supply_socket.recv(1024).decode('utf-8'))
supply_socket.sendall("ok".encode('utf-8'))

attacker_socket.sendall(dumper(msg4_data).encode('utf-8'))
ok = attacker_socket.recv(1024).decode('utf-8')

print(f"Recieved: Msg 4, session 1:")
print(msg4_data)
print()