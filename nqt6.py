'''
Find the number of cobinary palindromes existing between m and n
A cobinary palindrome is a number in which both the decimals number and its binary conversion
are palindrome.
for example, 313 is a palindrome and its binary 100111001 is also a palindrome.

'''
def convert_into_binary(number):
	return bin(number).replace("0b","")
def reverse_it(number):
	number = str(number)
	return number[::-1]
def is_palindrome(number):
	if number == int(reverse_it(number)) :
		return True
	else:
		return False
m = int(input("ENter starting number "))
n = int(input("Enter ending number"))
bin_pals = []
for i in range(m,n):
	if is_palindrome(i) == True and is_palindrome(int(convert_into_binary(i))):
		bin_pals.append(i)
print(bin_pals)
