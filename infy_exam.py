import string
import re
#ip = "HheLlOWoRldD"
ip = input("INput :- ")
#print("INput :-",ip)
ip_arr = []
word = list(string.ascii_letters) # list of alps, to itterate in loops and work as key in dict
words_dict = {} # dictionary of alps and no of time they repeat
test = []
test_low = []
test_up = []
finalword = []
ultra_final = []
final = ""



# index of repeated chars
for i in range(0,len(word)): # fill the dict like {'a':0,'b':0,...}
	words_dict.update({word[i]:0})

# Main Logic starts here
for i in range(0,len(ip)): # this loop will give occourence
	if ip[i] in word :
		words_dict[ip[i]] += 1
	else:
		print("Invalid characters in string")
# this will give a list of groups which are alphabetically arranged, first lower then all upper
for i in range(0,len(word)):
	if words_dict[word[i]] != 0 :
		 lol = word[i] * words_dict[word[i]]
		 test.append(lol)
#print("test",test)
# ['d', 'e', 'h', 'll', 'o', 'D', 'H', 'L', 'O', 'R', 'W']
for char in test:
	if char.islower() == True:
		test_low.append(char)
	elif char.isupper() == True:
		test_up.append(char)
for p in test_low:
	final = ""
	s = p[0]
	if s.upper() in test_up:
		x = test_up.index(s.upper())
		#print("{} is at index {} ".format(s.upper(),x))
		final =  p + test_up[x]
		#print(final)
		finalword.append(final)
finalword = test_low

def display(list):
	tester = []
	super_shit = []
	ultra_super_shit = ""
	tester.append(finalword[0])
	tester.append(finalword[-1])
	for i in range(1,len(finalword)):
		tester.append(finalword[i])
		z = -1 - i
		tester.append(finalword[z])
	q = len(tester)//2
	super_shit = tester[:q]
	#print(super_shit)
	yet_another_shit = ultra_super_shit.join(super_shit)
	print("Output :-",yet_another_shit)


display(finalword)

'''
test ['d', 'e', 'h', 'll', 'o', 'D', 'H', 'L', 'O', 'R', 'W']
test low ['d', 'e', 'h', 'll', 'o']
test up ['D', 'H', 'L', 'O', 'R', 'W']
finalword ['dD', 'hH', 'llL', 'oO']
'''













