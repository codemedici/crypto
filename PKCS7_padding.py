# solution 2_9 of matsano crypto challenges

def PKCS7(data, k=16):
    p = k - (len(data) % k)
    return data + chr(p)*p

print repr(PKCS7("YELLOW SUBMARINE", 20))
