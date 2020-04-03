n,m = map(int,input().split())

queries = []
array = [0] * n

print(array)
for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))
print(queries)


for i in range(0,3):
    a = queries[i][0]
    b = queries[i][1]
    k = queries[i][2]
    for j in range(a-1,b):
        array.remove(array[j])
        array.insert(j,array[j]+k)
    print(array)
