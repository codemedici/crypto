# Empirically prove that the keyspace of the affine cipher is limited to
# len(SYMBOLS) ^ 2.
# Forked from http://inventwithpython.com/hacking (BSD licensed).

import affine
from .cryptomath import gcd

message = 'Make things as simple as possible, but not simpler.'

for keyA in range(2, 100):
    key = keyA * len(affineCipher.SYMBOLS) + 1

    if gcd(keyA, len(affineCipher.SYMBOLS)) == 1:
        print(keyA, affine.encryptMessage(key, message))

