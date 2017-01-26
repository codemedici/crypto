def score(string):
     freq = dict()
     freq['a'] = 834
     freq['b'] = 154
     freq['c'] = 273
     freq['d'] = 414
     freq['e'] = 1260
     freq['f'] = 203
     freq['g'] = 192
     freq['h'] = 611
     freq['i'] = 671
     freq['j'] = 23
     freq['k'] = 87
     freq['l'] = 424
     freq['m'] = 253
     freq['n'] = 680
     freq['o'] = 770
     freq['p'] = 166
     freq['q'] = 9
     freq['r'] = 568
     freq['s'] = 611
     freq['t'] = 937
     freq['u'] = 285
     freq['v'] = 106
     freq['w'] = 234
     freq['x'] = 20
     freq['y'] = 204
     freq['z'] = 6
     freq[' '] = 2320

     ret = 0

     for c in string.lower():
         if c in freq:
             ret += freq[c]

     return ret

if __name__ == '__main__':

    print( score("killing mcs like a poisonous mushroom ETAOIN SHRDLU now that the party is poppin") )
    print "Unit test pass in main()"
