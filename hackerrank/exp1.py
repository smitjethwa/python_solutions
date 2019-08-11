"""
sock merchant
"""
import sys
from collections import Counter
n = int(input(""))
ar = input().split(' ')
#ar = [10,10,20,10,30]
pairs = {}
final = 0
# some validations
if len(ar) != n :
	print("invalid length of array")
	sys.exit()
for i in range(0,len(ar)):
	if int(ar[i]) < 1 :
		print("Number below 1 ")
		sys.exit()
	elif int(ar[i]) > 1000 :
		print("number above 1000")
		sys.exit
# All validations done
dic = Counter(ar) # count how many times an item is repeated in a list
for i in ar:
	if dic[i]%2 != 0 :
		lol = dic[i] -1
		lol = lol//2
		pairs.update({i:lol})
	else:
		lol = dic[i]
		lol = lol //2
		pairs.update({i:lol})
#print(pairs)
for p in pairs:
	final = final+pairs[p]
print(final)