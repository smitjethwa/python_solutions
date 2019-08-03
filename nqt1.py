'''
TCS NQT Coding 
________________________
the program will recieve 3 words from stdin
three words will be read one at a time, in three sepeate lines
first would should be changed like all vowels should be replaced by %
second word should be changed like all constants should be replaced by #
third word should change all char should be converted to upper case
then concat all the three words and print them
'''


class Magic:
	def __init__(self,word1,word2,word3):
		self.word1 = list(word1)
		self.word2 = list(word2)
		self.word3 = word3
		self.vowels = ["a","e","i","o","u"]

	def final_word1(self): # Convert vowels into #
		for alp in range(0,len(self.word1)):
			if self.word1[alp] in self.vowels:
				self.word1[alp] = "%"
			else:
				pass
		return ''.join(self.word1)

	def final_word2(self):	# Convert constants into #
		for alp in range(0,len(self.word2)):
			if self.word2[alp] in self.vowels:
				pass
			else:
				self.word2[alp] = "#"
		return ''.join(self.word2)
	
	def final_word3(self): # Converts into upper case
		return self.word3.upper()

	def compute(self): # Concat and Print
		word = self.final_word1() + self.final_word2() + self.final_word3()
		return(word)

word1 = str(input("Enter the first word\n"))
word2 = str(input("ENter the second word\n"))
word3 = str(input("Enter the third word\n"))

# Initialize Class
input = Magic(word1,word2,word3)
print(input.compute())