# Generate a series, such that even position will be series
# of Fibonacci series, and odd positions will be Prime Numbers.
# Example :- [0, 2, 1, 3, 1, 5, 2, 7] 
# Take input N from user and print the series upto N.  
# Alternate number will be a prime number and a fibonacci series


def fibonacci(n):
	if n<0 :
		print("Invalid")
	elif n == 0:
		return 0
	elif n==1 :
		return 1
	else:
		return fibonacci(n-1)+fibonacci(n-2)

def prime(num):
	if num > 1:  
		for i in range(2,num):  
			if (num % i) == 0:  
				break
		else:  
			primes.append(num)         
	else:  
		pass
n = int(input("enter N \n"))
fibos = []
primes = []
final = []
for i in range(0,n):
	fibos.append(fibonacci(i))
	prime(i)
#print(fibos)
#print(primes)
for i in range(0,len(primes)):
	one = fibos[i]
	two = primes[i]
	final.append(one)
	final.append(two)
print(final)

