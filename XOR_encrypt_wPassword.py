# Solution to Matasano Crypto challenge 1_5
# Repeating key XOR

def encryptMessage(message, password):

    passLen = len(password)
    xored = [] # variable to hold the xored string

    # iterate over the message in blocks with steps len(password)
    for blockStart in range(0, len(message), passLen):

        passRange = 0 # used for iterating over password len, resets every block
        # xor bytes of that particular block with the password
        # for the range of each block chose between len(message) is less then (blockstart + passlen), whichever is shorter

        for i in range(blockStart, min(blockStart + passLen, len(message))):
            xored.append( chr( ord(message[i])^ord(password[passRange]) ) )
            passRange = passRange + 1

    xored = ''.join(x for x in xored)
    return xored.encode('hex')


if __name__ == '__main__':

    p = "ICE"

    with open('data/5.txt', 'rb') as f:
        m = f.read().strip()

    # long way
    print encryptMessage(m, p)

'''
Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal
0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
key: ICE
'''
