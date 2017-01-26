import itertools
import vigenereCipher, freqAnalysis

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

dictionary = [ ''.join(c) for c in itertools.permutations(letters, 3) ]

ciphertext = "AZAXVHEFWVWOUWQCFEMHKARAZEJVNLCBFOVMMMBMSNHBAUGKZMBJGIEOWZWWWBYVLOZJLSUBIPDEYJXDGMBEYXSIKLNABQZNWTNTMAKZBNSRYJZYAPSFJNGRDXNAFOAWHO"

def main():
    topKey = []
    for k in dictionary:
        decrypted = vigenereCipher.decryptMessage(k,ciphertext)
        tuplekey = (k, freqAnalysis.englishFreqMatchScore(decrypted))
        topKey.append(tuplekey)
    topKey.sort(key=lambda x:x[1], reverse=True)
    for i in topKey[:4]:
        print i
        mess = vigenereCipher.decryptMessage(i[0],ciphertext)
        for j in range(0,len(mess),5):
            print mess[j:j+5],
        print


if __name__ == '__main__':

    main()
