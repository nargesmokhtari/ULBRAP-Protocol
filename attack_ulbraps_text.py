#In this Implementation, our primary assumption is that the Hash function was applied in CHR and CHT
#Then for AUTth, we used the XOR operation 

# MESG1
PR = '0xb26dccb2f47926ca931249d2e1a2f3100f4799b9'
CHR = '0x78c7d9693b1c94071f9f12f23ecbd6b1a276a225'
TIR = '0x193bc244'

#MESG2
CHT = '0x75962dbbec9945b0631fe44960730b34b7f20643'
AthR = '0xa55e9120ce1893623474dcb78b36befbaed52b8b'
PT = '0xdcccd3d45e7e90c2ee73d307639142eef1466716'
TIT = '0x193bc245'

#MESG3
PP =  '0xb639e22f8ae3bcf2402b5766a9ff495a6bfbbef9'
PQ =  '0x198e49ced2c2372bc48a763078786d2baa0eae6f'
Reader_check = '0xbddfe4047faa1ffb1e39ca5d58eb9c9950bad3bf'
TIR_prime = '0x193bc246'

#MESG4
SE = '0x0x3ef7fcec047b409667a2bf096e447db1752f2a03'
SF = '0xdff3b011ed02599e8afc25b911f6c6dd628bf9c0'
SG = '0x4368ebaad791ed061765241b406cb84378805ef2'
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

binary_TIS = '0b00011001001110111100001001000111'
SE = '0x3ef7fcec047b409667a2bf096e447db1752f2a03'
decimal_SE = int(SE, 16)
binary_SE_h = bin(decimal_SE)[2:]
binary_SE = binary_SE_h.rjust((160), '0')
print ( "binary_SE", binary_SE )

SF = '0xdff3b011ed02599e8afc25b911f6c6dd628bf9c0'
decimal_SF = int(SF, 16)
binary_SF_h = bin(decimal_SF)[2:]
binary_SF = binary_SF_h.rjust((160), '0')
print ( "binary_SF", binary_SF )

S0_candi_values= []
S0_candi_SF_values = []

all_values = []

for l in range (1 , 33):
  for m in range (1 , 161):
    rotated_TIS = left_rotate_binary(binary_TIS[2:], l)
    decimal_TIS = int (rotated_TIS, 2)
    rotated_S0 = hex(decimal_TIS ^ decimal_SE)
    decimal_rotated_S0 = int(rotated_S0, 16)
    binary_rotated_S0_h = bin(decimal_rotated_S0)[2:]
    binary_rotated_S0 = binary_rotated_S0_h.rjust((160), '0')
    print ( "binary_rotated_S0", binary_rotated_S0 )
    S0_camdi = left_rotate_binary(binary_rotated_S0, m)
    decimal_S0_candi = int (S0_camdi, 2)
    hex_number_S0_candi = hex(decimal_S0_candi)
    S0_candi_values.append(hex_number_S0_candi)
    #print (f" S0 candidate: {hex_number_S0_candi} ")

for j in range (1 , 33):
  for k in range (1 , 161):
    rotated_TIS_SF = left_rotate_binary(binary_TIS[2:], j)
    decimal_TIS_SF = int (rotated_TIS_SF, 2)
    rotated_S0_SF = hex(decimal_TIS_SF ^ decimal_SF)
    decimal_rotated_S0_SF = int(rotated_S0_SF, 16)
    binary_rotated_S0_SF_h = bin(decimal_rotated_S0_SF)[2:]
    binary_rotated_S0_SF = binary_rotated_S0_SF_h.rjust((160), '0')
    print ( "binary_rotated_S0", binary_rotated_S0_SF )
    S0_camdi_SF = left_rotate_binary(binary_rotated_S0_SF, m)
    decimal_S0_candi_SF = int (S0_camdi_SF, 2)
    hex_number_S0_candi_SF = hex(decimal_S0_candi_SF)
    S0_candi_SF_values.append(hex_number_S0_candi_SF)
    #print (f" S0 candidate: {hex_number_S0_candi_SF} ")
all_values = S0_candi_values + S0_candi_SF_values

len(S0_candi_values)

len(S0_candi_SF_values)

len(all_values)

all_values

PR_binary = '0b1011001001101101110011001011001011110100011110010010011011001010100100110001001001001001110100101110000110100010111100110001000000001111010001111001100110111001'
PT_binary = '0b1101110011001100110100111101010001011110011111101001000011000010111011100111001111010011000001110110001110010001010000101110111011110001010001100110011100010110'

TIR = '0x193bc244'
decimal_TIR = int(TIR, 16)
TIT = '0x193bc245'
decimal_TIT = int(TIT, 16)

BalN = '0xab03cbdeb5a7764b6732c417cbf8a0a4407d6f54'
decimal_BalN = int(BalN, 16)
binary_BalN_h = bin(decimal_BalN)[2:]
binary_BalN = binary_BalN_h.rjust((160), '0')
print ( "binary_BalN", binary_BalN )

import hashlib
from hashlib import sha1

IDNt_XOR_IDNs_list = []
for X in all_values:
  for i in range (1 , 161):
    for j in range (1, 161):
      rotated_PR = left_rotate_binary( PR_binary[2:] , i )
      decimal_PR = int (rotated_PR, 2)
      R0_XOR_IDNt = hex(decimal_PR ^ decimal_TIR)
      decimal_R0_XOR_IDNt = int (R0_XOR_IDNt , 16)

      rotated_PT = left_rotate_binary( PT_binary[2:] , j )
      decimal_PT = int (rotated_PT, 2)
      R0_XOR_IDNs = hex(decimal_PT ^ decimal_TIT)
      decimal_R0_XOR_IDNs = int (R0_XOR_IDNs , 16)
      IDNt_XOR_IDNs = hex (decimal_R0_XOR_IDNt ^ decimal_R0_XOR_IDNs)
      IDNt_XOR_IDNs_list.append(IDNt_XOR_IDNs)
      decimal_IDNt_XOR_IDNs = int(IDNt_XOR_IDNs, 16)

      TKST_h = hex((int(X, 16)) ^ decimal_IDNt_XOR_IDNs ^ decimal_BalN)[2:]
      print (TKST_h)
      print(int(X, 16) , decimal_IDNt_XOR_IDNs)
      padding_hash_TKST = TKST_h.rjust((40), '0')
      print (padding_hash_TKST)


      # Calculate SHA-1 hash
      hash_TKST_h = sha1(bytes.fromhex(padding_hash_TKST))
      hx_TKST_h = hash_TKST_h.hexdigest()
      print('TKST: ', hx_TKST_h)

      decimal_TKST = int(hx_TKST_h, 16)
      binary_TKST_h = bin(decimal_TKST)[2:]
      binary_TKST = binary_TKST_h.rjust((160), '0')
      print ( "binary_TKST", binary_TKST )

      concatenated_hex_SG = binary_TKST +  bin(int(X, 16))[2:].rjust((160), '0') + binary_BalN

      decimal_number_concatenated_hex_SG = int (concatenated_hex_SG, 2)
      hex_number_concatenated_hex_SG = hex(decimal_number_concatenated_hex_SG)
      print ( "concatenated_Binary_SG : " ,concatenated_hex_SG)
      print ( "SG : " , hex_number_concatenated_hex_SG)

len(IDNt_XOR_IDNs_list)

