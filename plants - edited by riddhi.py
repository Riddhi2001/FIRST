n = int(input())
plant = list(map(int,input().split()))
count = 0
dead_plant = []


for i in range(1,n):
    if plant[i] > plant[i - 1]:
        dead_plant.append(plant[i])
print(dead_plant)       #prints dead plants of day 1
for i in dead_plant: #removes dead plant from day 1
    try: 
        plant.remove(i) 
    except ValueError: 
        pass
print(plant) #prints remaining plants of day 1

#we have to put all this in one big loop so that the remaining list of plant goes through the same process again.
#we have to modify the code to run for until there are no more deaths.
