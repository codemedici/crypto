# Caesar Cipher Hacker
# Forked from http://inventwithpython.com/hacking (BSD licensed).

# Brute force test each key in the cipher.

CHARACTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

def main():

    message = input('Enter a message: ')

    hackCaesarCipher()


def caesarCipher(message, key, mode):

    translated = ''

    for symbol in message:
        if symbol in CHARACTERS:
            num = CHARACTERS.find(symbol)
            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = num - key

            if num >= len(CHARACTERS):
                num = num - len(CHARACTERS)
            elif num < 0:
                num = num + len(CHARACTERS)

            translated = translated + CHARACTERS[num]

        else:
            translated = translated + symbol

    print('Key #%s: %s' % (key, translated))

def hackCaesarCipher(message):

    for key in range(len(CHARACTERS)):
        caesarCipher(message, key, 'decrypt')

if __name__ == '__main__':
    main()












