#!/usr/local/bin/python


class Deck:
	# Sets up the Deck in Bridge format
	def __init__(self):
		self.Cards = []
		for i in range(1,55):
			self.Cards.append(i)

	def MoveDownOne(self, index):
		if (index == 53):
			temp = self.Cards[index]
			self.Cards[index] = self.Cards[0]
			self.Cards[0] = temp
		else:
			temp = self.Cards[index]
			self.Cards[index] = self.Cards[index + 1]
			self.Cards[index + 1] = temp

	def MoveDownTwo(self, index):
		if (index == 53):
			self.Cards.insert(2, self.Cards[index])
			del self.Cards[index + 1]
		elif (index == 52):
			self.Cards.insert(1, self.Cards[index])
			del self.Cards[index + 1]
		else:
			self.Cards.insert((index + 3), self.Cards[index])
			del self.Cards[index]

	def GetValueByIndex(self, index):
		return self.Cards[index]

	def GetIndexByValue(self, value):
		for i in range(0,54):
			if (self.Cards[i] == value):
				return i
		return -1

	def TripleCut(self, low, high):
		self.Cards = self.Cards[high + 1:] + self.Cards[low:high + 1] + self.Cards[:low]

	def CountCutByIndex(self, index):
		CutBy = index
		self.Cards = self.Cards[CutBy:-1] + self.Cards[:CutBy] + [self.Cards[53]]



class SolitaireCipher:
	def __init__(self):
		self.Deck = Deck()

	def GetNextOutput(self):
		self.Deck.MoveDownOne(self.Deck.GetIndexByValue(53))

		self.Deck.MoveDownTwo(self.Deck.GetIndexByValue(54))

		if (self.Deck.GetIndexByValue(53) > self.Deck.GetIndexByValue(54)):
			self.Deck.TripleCut(self.Deck.GetIndexByValue(54), self.Deck.GetIndexByValue(53))
		else:
			self.Deck.TripleCut(self.Deck.GetIndexByValue(53), self.Deck.GetIndexByValue(54))

		CutBy = self.Deck.Cards[53]
		if (CutBy == 54):
			CutBy = 53
		self.Deck.CountCutByIndex(CutBy)

		TopCard = self.Deck.Cards[0]
		if (TopCard == 54):
			TopCard = 53
		return (self.Deck.Cards[TopCard])

	def KeyDeck(self, s):
		from string import upper, letters
		k = ""
		for i in range(0, len(s)):
			if s[i] in letters:
				k = k + s[i]
		k = upper(k)
		for i in range(0, len(s)):
			self.GetNextOutput()
			# New Step Five
			self.Deck.CountCutByIndex(ord(k[i]) - 64)

	def Encrypt(self, s):
		from string import upper, letters
		c = ""
		p = ""
		for i in range(0, len(s)):
			if s[i] in letters:
				p = p + s[i]
		p = upper(p)
		if not ((len(p) % 5) == 0):
			p = p + ('X' * (5 - (len(p) % 5)))
		for j in range(0, len(p)):
			while(1):
				output = self.GetNextOutput()
				if ((output == 53) or (output == 54)):
					continue
				else:
					break
			if (output > 26):
				output = output - 26
			k = (ord(p[j]) - 65) + output
			if (k > 25):
				k = k - 26
			k = k + 65
			c = c + chr(k)
		return c

	def Decrypt(self, s):
		from string import upper, letters
		c = ""
		p = ""
		for i in range(0, len(s)):
			if s[i] in letters:
				c = c + s[i]
		c = upper(c)

		for j in range(0, len(c)):
			while(1):
				output = self.GetNextOutput()
				if ((output == 53) or (output == 54)):
					continue
				else:
					break

			if (output > 26):
				output = output - 26
			k = ord(c[j]) - output
			if (k < 65):
				k = k + 26
			p = p + chr(k)

		return p

def PrintInFives(s):
	ns = ""
	for i in range(0,len(s)):
		ns = ns + s[i]
		if (len(ns) == 5):
			print ns,
			ns = ""
	print ns

def test():
	print "Running Test Vectors"
	print "--------------------"
	# (plaintext, key, ciphertext)
	vectors = [
				("AAAAAAAAAAAAAAA", "", "EXKYIZSGEHUNTIQ"),
				("AAAAAAAAAAAAAAA", "f", "XYIUQBMHKKJBEGY"),
				("AAAAAAAAAAAAAAA", "foo", "ITHZUJIWGRFARMW"),
				("AAAAAAAAAAAAAAA", "a", "XODALGSCULIQNSC"),
				("AAAAAAAAAAAAAAA", "aa", "OHGWMXXCAIMCIQP"),
				("AAAAAAAAAAAAAAA", "aaa", "DCSQYHBQZNGDRUT"),
				("AAAAAAAAAAAAAAA", "b", "XQEEMOITLZVDSQS"),
				("AAAAAAAAAAAAAAA", "bc", "QNGRKQIHCLGWSCE"),
				("AAAAAAAAAAAAAAA", "bcd", "FMUBYBMAXHNQXCJ"),
				("AAAAAAAAAAAAAAAAAAAAAAAAA", "cryptonomicon", "SUGSRSXSWQRMXOHIPBFPXARYQ"),
				("SOLITAIRE","cryptonomicon","KIRAKSFJAN")
				]
	for i in vectors:
		s = SolitaireCipher()
		s.KeyDeck(i[1])
		ciphertext = s.Encrypt(i[0])
		if (ciphertext == i[2]):
			print "passed!"
		else:
			print "FAILED!"
		print "plaintext           = " + i[0]
		print "key                 = " + i[1]
		print "expected ciphertext =",
		PrintInFives(i[2])
		print "got ciphertext      =",
		PrintInFives(ciphertext)
		print
	print "Test bijectivity (i.e. make sure that D(E(m)) == m"
	print "--------------------------------------------------"
	from whrandom import choice, randint
	from string import uppercase
	for i in range(0,5):
		p = ""
		for i in range(0,randint(10,25)):
			p = p + choice(uppercase)
		s = SolitaireCipher()
		s.KeyDeck("SECRETKEY")
		c = s.Encrypt(p)
		s = SolitaireCipher()
		s.KeyDeck("SECRETKEY")
		r = s.Decrypt(c)
		if (r[:len(p)] == p):
			print "passed!"
		else:
			print "FAILED!"
		print "Random plaintext =",
		PrintInFives(p)
		print "ciphertext       =",
		PrintInFives(c)
		print "decrypt          =",
		PrintInFives(r[:len(p)])

		print





if (__name__ == "__main__"):
	from sys import argv
	from string import upper
	usage = "Usage:\nsolitaire.py [-test] | [-e,-d] key filename\n"

        Ciphertext = "AZAXV HEFWV WOUWQ CFEMH KARAZ EJVNL CBFOV MMMBM SNHBA UGKZM BJGIE OWZWW WBYVL OZJLS UBIPD EYJXD GMBEY XSIKL NABQZ NWTNT MAKZB NSRYJ ZYAPS FJNGR DXNAF OAWHO"
        s = SolitaireCipher()
        s.KeyDeck("cosimo")
        Plaintext = s.Decrypt(Ciphertext)
        PrintInFives(Plaintext)

'''
	if (len(argv) < 2):
		print usage
	elif ("-TEST" in map(upper,argv)):
		test()
	elif (upper(argv[1]) == "-E"):
		FileToEncrypt = open(argv[3])
		Plaintext = FileToEncrypt.read()
		s = SolitaireCipher()
		s.KeyDeck(argv[2])
		Ciphertext = s.Encrypt(Plaintext)
		PrintInFives(Ciphertext)
	elif (upper(argv[1]) == "-D"):
		FileToDecrypt = open(argv[3])
		Ciphertext = FileToDecrypt.read()
		s = SolitaireCipher()
		s.KeyDeck(argv[2])
		Plaintext = s.Decrypt(Ciphertext)
		PrintInFives(Plaintext)
	else:
		print usage
                '''
