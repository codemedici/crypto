# solution 2_15 of matasano crypto challenges

class PaddingError(Exception):
    pass

def remove_PKCS7(m):

    l = len(m)
    p = ord(m[l-1])

    if p > l or p == 0: # p must be an in in range 0 < p < l
        raise PaddingError()

    for i in range(l-p, l):
        if ord(m[i]) != p: # If any of the bytes isn't the padding byte
            raise PaddingError()

    print m[:-p] # slice message part and remove padding

valid = "ICE ICE BABY\x04\x04\x04\x04"
#invalid = "ICE ICE BABY\x00"
#invalid1 = "ICE ICE BABY\x05\x05\x05\x05"
#invalid2 = "ICE ICE BABY\x01\x02\x03\x04"

remove_PKCS7(valid)
