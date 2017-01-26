# Solution to Matasano Crypto challenge 1_6

from common import score, hamming
from itertools import cycle

with open('data/6.txt', 'r') as f:
    m = f.read().decode('base64')


def xor(encrypted, k):
    # single byte XOR
    return ''.join(chr(ord(e) ^ k) for e in encrypted)


def normalized_distance(keysize):
    blocks = len(m) / keysize
    distance = 0

    for i in range(blocks-1):
        x = m[ i*keysize : (i+1)*keysize ]
        y = m[ (i+1)*keysize : (i+2)*keysize ]
        distance += hamming(x,y)
    # average the total distance by the number of blocks
    distance /= float(blocks) # float to be more accurate
    # normalize the distance by dividing by keysize
    distance /= float(keysize)
    return distance

#most likely keysize is the one with the smallest normalized distance
keysize = min(range(2,40), key=normalized_distance)
print "Most likely key size is ", keysize

key = [None]*keysize

for i in range(keysize):
    # string composed by every ith symbol in every data block of keysize
    d = m[i::keysize]
    # for each string of ith symbols, sigle key XOR with every 256 ascii character
    # return the character which yields the highest 'ETAOIN' score
    key[i] = max(range(256), key = lambda k: score(xor(d, k)))

# convert the ascii numbers into a string of symbols
key = ''.join(map(chr, key))

print "KEY = ", repr(key)
print

# repeating key XOR
print ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(m, cycle(key)))
