# Solution to Matasano Crypto challenge 1_7

from Crypto.Cipher import AES

KEY = "YELLOW SUBMARINE"

with open('data/7.txt', 'r') as f:
    c = f.read().decode('base64')

def AES_ECB_decrypt(c):
    cipher = AES.new(KEY, AES.MODE_ECB)
    return cipher.decrypt(c)

print AES_ECB_decrypt(c)
