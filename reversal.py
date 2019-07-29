'''
Various ways to reverse a List, or a string

'''

def rev_using_slice(word):
	return(word[::-1])
def rev_using_for(word):
	lol = ''
	for chars in word:
		lol = chars+lol
	return(lol)
def using_list(s):
    lol = list(s)
    lol.reverse()
    return ''.join(lol)

word = "reversal" #word to be reversed
print(" Reverse Using Slice \t",rev_using_slice(word))
print(" Reverse Using For Loop \t",rev_using_for(word))
print(" Reverse Using List to reverse \t",using_list(word))
