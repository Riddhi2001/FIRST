n=int(input())
x=n
plant = list(map(int,input().split()))
days=0
count=0

while x != 0:
    death=[]
    x -= 1
    temp=len(death)
    for i in range(1,n-count):
        if plant[i] > plant[i-1] :
            death.append(plant[i])
            count += 1

    if len(death) == temp:
        break
    else :
        days += 1
        for i in death:
            plant.remove(i)

#print('Number of days after which no plants will die=',days)
#print('Survivor plants=',plant)
print(days)









       
            
        
