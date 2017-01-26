from itertools import cycle

p = "ICE"
m = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"

print ''.join( chr( ord(x) ^ ord(y) ) for x, y in zip(m, cycle(p)) ).encode('hex')
