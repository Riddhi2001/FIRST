n=int(input())
x=n
plant = list(map(int,input().split()))
days=0
count=0


while x != 0:
    death =[]
    x -= 1
    temp=len(death)
    for i in range(1,n-count):
        if plant[i] > plant[i-1] :
            death.append(i)
            count += 1
    print(death)

    if len(death) == temp:
        break
    else :
        days += 1
        for i in reversed(death) :
            #x=plant[i]
            #plant.remove(plant[x])
            del(plant[i])
        print(plant)

print('Number of days after which no plants will die=',days)
print('Survivor plants=',plant)










       
            
        
