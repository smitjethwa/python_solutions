"""
Write a program to print all the LEADERS in the array. 
An element is leader if it is greater than all the elements to its right side. 
And the rightmost element is always a leader. 
For example int the array {16, 17, 4, 3, 5, 2},
 leaders are 17, 5 and 2.

"""
def SplitIt(SomeList):
	for i in range(0,len(SomeList)):
		try:
			maxm = max(SomeList)
			leaders.append(maxm)
			SomeList = SomeList[SomeList.index(maxm)+1:len(SomeList)]
			SplitIt(SomeList)
		#	print(leaders)
		except:
		#	print("Error !")
			pass
			
ip = [16,19,4,3,8,3]
leaders = []
lol = []

SplitIt(ip)
lol = set(leaders)
print(lol)
