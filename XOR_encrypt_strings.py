# Solution to Matasano Crypto challenge 1_2

def unhexor(a,b):
    assert len(a) == len(b)
    return ''.join(chr(ord(x)^ord(y)) for x,y in zip(a,b))

if __name__ == '__main__':

    s1 = "1c0111001f010100061a024b53535009181c"
    # ^
    s2 = "686974207468652062756c6c277320657965"
    # ==
    # 746865206b696420646f6e277420706c6179

    try: # if it is hex decode it
        s1 = s1.decode('hex')
        s2 = s2.decode('hex')
    except: # else leave as it is
        pass

    # equal len string XOR
    xored = unhexor(s1,s2)

    print xored
    assert xored.encode('hex') == "746865206b696420646f6e277420706c6179"
