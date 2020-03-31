n=int(input())
count=0

lst=[int(x) for x in input().split()]

deaths = len(lst)

temp = 0
while deaths != temp:
        temp = deaths

        for i in range (1,n+1-count) :
                if lst[i] > lst[i-1]:
                        del(lst[i])
                        count += 1
                        deaths -= 1
                        #n= len(lst)
                        
                else:
                        continue
                
                print(lst)
                n=len(lst)
                break

print('Number of days after which no plants will die=',count)
