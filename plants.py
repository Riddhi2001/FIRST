n=int(input())
count=0
lst=[int(x) for x in input().split()]
for i in range (1,n+1) :
    while lst[i] > lst[i-1] :
        for i in range (1,n+1) :
            del(lst[i])
            count += 1
    
    print(lst)

print('Number of days after which no plants will die=',count)
