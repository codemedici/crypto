from freqAnalysis import score

s = "some long-ass text, to allow frequency analysis to detect key length"

scores = []
for k in range(2,20):
    key = []
    for i in range(0,len(s),k):
        key.append(s[i])
    seq = ''.join(key)
    scores.append( (score(seq), k, seq) )

keysize = max(scores)[1]

#example use
'''
from caesarHacker import hackCaesarCipher
for i in range(keysize):
    d = s[i::keysize]
    print d
    print hackCaesarCipher(d)
    print
'''
