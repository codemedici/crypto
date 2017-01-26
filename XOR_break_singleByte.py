# Solution to Matasano Crypto challenge 1_3

from Crypto.Util.strxor import strxor_c
from common import score

def hexor256(s):

    # make a list of tuples with score of each strxor and int value used for xor [(score, int),..]
    # get the tuple with highest score value
    # max() finds the tuple with highest value at index 0
    # xor string again with highest score int to avoid storing a huge dict like [(score, strxor)..]
    return strxor_c( s, max( [ (score(strxor_c(s, i)), i) for i in range(256) ] )[1] )

if __name__ == '__main__':

    encoded = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    # c = '6574616f696e20736872646c75'
    s = encoded.decode('hex')

    print hexor256(s)
