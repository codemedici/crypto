def hamming(x,y):

    assert len(x) == len(y)
    x = x.encode('hex')
    y = y.encode('hex')

    count, z = 0, int(x,16)^int(y,16)
    while z:
        count += 1
        z &= z-1
    return count

if __name__ == '__main__':

    #x =''.join('{0:08b}'.format(ord(x), 'b') for x in a)
    #y =''.join('{0:08b}'.format(ord(x), 'b') for x in b)
    a = "this is a test"
    b = "wokka wokka!!!"

    assert(hamming(a,b) == 37)
    print "Unit test pass in main()"
