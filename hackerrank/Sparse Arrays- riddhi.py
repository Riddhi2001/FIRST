strings_num = int(input())
string = []
for i in range(strings_num):
    string.append(input())

query_num = int(input())
query = []
for i in range(query_num):
    query.append(input())

print(string,query)

for i in query:
    print(string.count(i))
        
