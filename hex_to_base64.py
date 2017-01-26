# solution to Matasano Crypto challenge 1_1

# s = string to convert
s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

#  Always operate on raw bytes, never on encoded strings.
ice = s.decode('hex') # "I'm killing your brain like a poisonous mushroom"

# Only use hex and base64 for pretty-printing.
b64 = s.decode('hex').encode('base64').rstrip() # "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
