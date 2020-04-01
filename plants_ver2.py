n=int(input())
count=0
a=[]

lst=[int(x) for x in input().split()]

deaths = n

temp = 0
while deaths != temp:
    temp = deaths

    for i in range(1,n+1-count):
        if lst[i] > lst[i-1]:
            a.append(i)
            count += 1
            deaths -= 1
            print(a)
        for x in a:
            del(lst[x])

        print(lst)
        n=len(lst)
        break

print('NO. of days after which no plants will die =',count)
