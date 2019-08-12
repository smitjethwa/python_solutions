'''
You are given a string, print the Nth term, or series upto Nth term
1,1,2,3,4,9,8,27,16,81,32,243,64,729,128,2187

first series  : 1,2,4,8,16,32,64,128,  --> 2 ^ (i++) series in even term
second series : 1,3,9,27,81,243,729,2187 --> 3 ^ (i++)series in odd term

'''
def compute(n):
	even = 0
	odd = 0
	series = []
	for i in range(0,n):
		if (i%2 == 0):
			series.append(pow(2,even))
			even += 1
		elif (i%2 != 0):
			series.append(pow(3,odd))
			odd += 1
	return(series)

n = int(input("Enter the N\n"))
print(compute(n))