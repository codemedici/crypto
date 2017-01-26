# Caesar Cipher
# Forked from http://inventwithpython.com/hacking (BSD licensed).

def main():
 
    message = input('Enter a message: ')
    key = input('Enter the key: ')
    mode = input('Enter mode (decrypt or encrypt): ')
  
    caesarCipher(message, key, mode)


def caesarCipher(message, key, mode):
# Run encryption/decryption on each symbol in the message string.

    CHARACTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    key = int(key)
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

    print(translated)

if __name__ == '__main__':
    main()










