"""
TCS Ninja | coding
you are given a series like
0 0 2 1 4 2 6 3 8 4 10 5 12 6 14 7 16 8  ....can go upto N

find the Nth term, or print upto Nth term

index :- 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
term :-  0 0 2 1 4 2 6 3 8 4 10 5  12  6 14 7 

Even terms is multiple of 2 series..
Odd term is 0,1,2,3,4,5,6,7

"""
def calc(n):
	ip = []
	even = 0
	odd = 0
	for i in range(0,n):
		if i%2 == 0:
			ip.append(even)
			even += 2
		elif i%2 != 0:
			ip.append(odd)
			odd += 1
	return(ip)

n = int(input("Enter the Nth term\n"))
print(calc(n))