n = int(input())
plant = list(map(int,input().split()))
count = 0
dead_plant = []
len_p = n
len_d_p = 0
temp = 0
days = 0
while True:
   
    temp = len_p
    for i in range(1,n - len_d_p):
        if plant[i] > plant[i-1]:
            dead_plant.append(i)

      
    len_d_p += len(dead_plant)
    #print('dead plant on day no.',days,dead_plant,len_d_p) 

    for i in reversed(dead_plant): 
        try:
        
            del(plant[i])
        except ValueError:
            pass
    dead_plant.clear()
    len_p = len(plant)
    if len_p != temp:
        days += 1
    else:
        break
print(days)

