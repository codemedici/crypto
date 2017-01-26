# Affine Cipher
# Forked from http://inventwithpython.com/hacking (BSD licensed).

import sys, random
from ..cryptomath.gcd import euclid
from ..cryptomath.extendedEuclid import findModInverse
SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def main():
    message = """"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing"""
    key = getRandomKey()
    mode = 'encrypt'

    if mode == 'encrypt':
        translated = encryptMessage(key, message)
    elif mode == 'decrypt':
        translated = decryptMessage(key, message)
    print('Key: %s' % (key))
    print('%sed text:' % (mode.title()))
    print(translated)


def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)


def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('The affine cipher is weak when key A is set to 1. Choose a different key.')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('The affine cipher is weak when key B is set to 0. Choose a different key.')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s. Choose a different key.' % (len(SYMBOLS) - 1))
    if euclid(keyA, len(SYMBOLS)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(SYMBOLS)))


def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    ciphertext = ''

    for symbol in message:
        if symbol in SYMBOLS:
            # Encrypt this symbol.
            symIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            # Otherwise append unencrypted symbol.
            ciphertext += symbol

    return ciphertext


def decryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plaintext = ''
    modInverseOfKeyA = findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            # Decrypt this symbol.
            symIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            # Otherwise append undecrypted symbol.
            plaintext += symbol

    return plaintext


def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if euclid(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB


if __name__ == '__main__':
    main()





