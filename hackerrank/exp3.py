n = int(input())
some_list = list(map(int, input().split()))
some_list.append(0)
some_list.append(0)
final = 0
count = 0
while final<=n-2:
    if some_list[final+1]!=1 and some_list[final+2]!=1:
        final+=2
    elif some_list[final+1]!=1 and some_list[final+2]==1:
        final+=1
    elif some_list[final+1]==1 and some_list[final+2]!=1:
        final+=2
    count+=1
print(count)