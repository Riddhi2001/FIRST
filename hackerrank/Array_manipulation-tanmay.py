n,m=[int(i) for i in input().split()]
#print(n,m)
array=[]
for i in range(n):
    array.append(0)
#print(array)
for i in range(m):
    a,b,k=[int(i) for i in input().split()]
    for i in range(a,b+1):
        array[i-1] += k
print(max(array))
