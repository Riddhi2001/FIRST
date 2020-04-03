n=int(input())
string=[]
queries=[]
for i in range(n):
    string.append(input())

l=int(input())
for i in range(l):
    queries.append(input())

for i in range(l):
    print(string.count(queries[i]))




