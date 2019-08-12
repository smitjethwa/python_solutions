# author : smitjethwa

a = input().split()
m = int(a[0])
n = int(a[1])

prime_list = []

def check_prime(a):
    k=0
    for i in range(2,a//2+1):
        if(a%i==0):
            k=k+1
    if(k<=0):
        return True
    else:
        return False
        

for i in range(m,n+1):
    if check_prime(i):
        prime_list.append(i)
    
count = 0
for a in prime_list:
    b = a + 6
    if b in prime_list:
        count = count + 1

print(count)
