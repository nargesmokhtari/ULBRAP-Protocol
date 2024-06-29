#Traceability attack

# MESG1
PR = '0xb26dccb2f47926ca931249d2e1a2f3100f4799b9'
CHR = '0xb69dc64f774510d660958b982dcdc80fe7806179'
TIR = '0x193bc244'

#MESG2
CHT = '0x33dd77ec98e7ab7d245dce4c0d8b1f747f768603'
PT = '0xdcccd3d45e7e90c2ee73d307639142eef1466716'
TIT = '0x193bc245'

#MESG4
SE = '0x1f7bfe76023da04b33d15f84b7223ed8a3fcfabb'
SF = '0xdff3b011ed02599e8afc25b911f6c6ddd88403dc'
SG = '0x8928b7b5cb1108ac41e1ba11aaffc9aac8a00a67'
TIS = '0x193bc247'

# Function to count non-zero elements in binary number
def count_non_zero_elements(binary_number):
    count = 0
    for digit in binary_number:
        if digit == '1':
            count += 1
    return count

# rotation operation
def left_rotate_binary(binary_number, positions):
    binary_length = len(binary_number)
    positions %= binary_length  # Ensure positions are within the length of the binary number

    # Perform left rotation
    rotated_number = binary_number[positions:] + binary_number[:positions]
    return rotated_number

TIR = '0x193bc244'
decimal_TIR = int(TIR, 16)
TIT = '0x193bc245'
decimal_TIT = int(TIT, 16)
PR = '0xb26dccb2f47926ca931249d2e1a2f3100f4799b9'
decimal_PR_real_value = int(PR, 16)

import hashlib
from hashlib import sha1

PR_binary = '0b1011001001101101110011001011001011110100011110010010011011001010100100110001001001001001110100101110000110100010111100110001000000001111010001111001100110111001'

for i in range (1,161):
  rotated_PR = left_rotate_binary( PR_binary[2:] , i )
  decimal_PR = int (rotated_PR, 2)
  R0_XOR_IDNt = hex(decimal_PR ^ decimal_TIR)
  decimal_R0_XOR_IDNt = int (R0_XOR_IDNt , 16)
  print ( R0_XOR_IDNt)
  h1 = hex (decimal_R0_XOR_IDNt ^ decimal_PR_real_value)
  print (h1)
  str_CHR_loop = h1[2:]
  result_CHR_loop = hashlib.sha1(str_CHR_loop.encode())
  CHR_loop = result_CHR_loop.hexdigest()
  print(CHR_loop)
  if CHR_loop == CHR[2:] :
    break
print (" R0_XOR_IDNt : " , R0_XOR_IDNt)
print ( i)
R0_XOR_IDNt = R0_XOR_IDNt

R0_XOR_IDNt = '0x49274b868bcc403d1e66e6c9b732cbd1fda0e808'
decimal_R0_XOR_IDNt = int(R0_XOR_IDNt, 16)
PT_binary = '0b1101110011001100110100111101010001011110011111101001000011000010111011100111001111010011000001110110001110010001010000101110111011110001010001100110011100010110'

IDNt_XOR_IDNs_First_session = []
for j in range (1, 161):
  rotated_PT = left_rotate_binary( PT_binary[2:] , j )
  decimal_PT = int (rotated_PT, 2)
  R0_XOR_IDNs = hex(decimal_PT ^ decimal_TIT)
  decimal_R0_XOR_IDNs = int (R0_XOR_IDNs , 16)
  IDNt_XOR_IDNs = hex (decimal_R0_XOR_IDNt ^ decimal_R0_XOR_IDNs)
  IDNt_XOR_IDNs_First_session.append(IDNt_XOR_IDNs)
  print ( IDNt_XOR_IDNs)

#second session

TIR = '0x62599048'
decimal_TIR = int(TIR, 16)
TIT = '0x62599049'
decimal_TIT = int(TIT, 16)
R0 = '0x5f16fa1003bb8fc89a50deaa1faa1bc423cd37d6'
IDNt = '0x32090fde402efd4495f755ab3ee16c16e6d249dd'
IDNs = '0xe5b67f4441f5caf3b8a90584ef4d0534f6cf74e3'
BalN = '0xab03cbdeb5a7764b6732c417cbf8a0a4407d6f54'

# R0 ^ IDNt
R0XORIDNt = hex (0x5f16fa1003bb8fc89a50deaa1faa1bc423cd37d6 ^0x32090fde402efd4495f755ab3ee16c16e6d249dd )
print (R0XORIDNt )

# R0 ^ IDNs
R0XORIDNs = hex (0x5f16fa1003bb8fc89a50deaa1faa1bc423cd37d6 ^ 0xe5b67f4441f5caf3b8a90584ef4d0534f6cf74e3)
print (R0XORIDNs)

PR = '0x8b01214b77d2a746ee436d1ff5ce4395728c0fa7'

PT = '0xed9778738f785bade9be5d5042aa2127229d917c'

PR_binary = '0b1000101100000001001000010100101101110111110100101010011101000110111011100100001101101101000111111111010111001110010000111001010101110010100011000000111110100111'
PT_binary = '0b1110110110010111011110000111001110001111011110000101101110101101111010011011111001011101010100000100001010101010001000010010011100100010100111011001000101111100'

R0XORIDNt= '0x6d1ff5ce4395728c0fa78b01214b77d2c51f7e0b'
decimal_R0XORIDNt = decimal_TIR = int(R0XORIDNt, 16)

IDNt_XOR_IDNs_Second_session = []
for k in range (1, 161):
  rotated_PT = left_rotate_binary( PT_binary[2:] , k )
  decimal_PT = int (rotated_PT, 2)
  R0_XOR_IDNs = hex(decimal_PT ^ decimal_TIT)
  decimal_R0_XOR_IDNs = int (R0_XOR_IDNs , 16)
  IDNt_XOR_IDNs = hex (decimal_R0XORIDNt ^ decimal_R0_XOR_IDNs)
  IDNt_XOR_IDNs_Second_session.append(IDNt_XOR_IDNs)
  print ( IDNt_XOR_IDNs)

# Convert the lists to sets
set1 = set(IDNt_XOR_IDNs_First_session)
set2 = set(IDNt_XOR_IDNs_Second_session)

# Find the common elements
common_elements = set1.intersection(set2)

# Print the common elements
print("Common elements:", common_elements)

