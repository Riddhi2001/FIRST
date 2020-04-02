n = int(input())
plant = list(map(int,input().split()))
count = 0
dead_plant = []
len_p = 1
len_d_p = 0
while True:
    print('1')
    for i in range(1,n - len_d_p):
        if plant[i] > plant[i - 1]:
            dead_plant.append(plant[i])

      
    len_d_p = len(dead_plant)
    print(dead_plant,len_d_p) 
    for i in dead_plant: 
        try: 
            plant.remove(i) 
        except ValueError: 
            pass
    len_p = len(plant)
    print(plant,len_p)
print('2')
