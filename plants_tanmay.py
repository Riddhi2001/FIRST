n=int(input())
count=0
a=[]

lst=[int(x) for x in input().split()]

deaths = len(lst)

temp = 0
while deaths != temp:
        temp = deaths

        for i in range(1,n+1-count):
            if lst[i] > lst[i-1]:
                a.append(i)
                count += 1
                deaths -= 1

            for i in range (count):
                x=a[i]
                del(lst[x])

            print(lst)
            n=len(lst)
            break

print('Number of days after which no plants will die=',count)
        

