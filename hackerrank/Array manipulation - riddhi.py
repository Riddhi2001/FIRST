n,m = map(int,input().split())

queries = []
array = [0] * n

#print(array)

for i in range(0,m):
    a,b,k=map(int,input().split())

    for j in range(a-1,b):
        
        array[j] += k
print(max(array))
