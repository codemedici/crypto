# Solution to Matasano Crypto challenge 1_4

from Crypto.Util.strxor import strxor_c
from common import score

def hexor256(s):
    return max( [ (score(strxor_c(s, i)), i) for i in range(256) ] )


def xorLines(lst):
    # return a list of nested tuples, each line is a nested tuple in form
    # [ ((best score, ascii int), line number), .. ]
    # line is the nested tuple with highest score value
    # using range so not to store entire lines in the list but just line number
    line =  max( [ (hexor256(lst[i]), i) for i in range(len(lst))] )

    # xor the hex decoded line with the int value returned by hexor256
    return strxor_c(lst[line[1]], line[0][1]).strip()


if __name__ == '__main__':

    # One of the 60-character strings in this file has been encrypted by single-character XOR.
    data = 'data/4.txt'

    with open(data, 'r') as f:
        lst = f.readlines()

    lst = [i.strip().decode('hex') for i in lst]

    print xorLines(lst)
