n=int(input())

data=list(map(int,input().split(',')))
x=len(data)
width=[]

for i in reversed(range(0,x,2)):
    width.append(data[i])
    del(data[i])

w=max(width)
h=max(data)

max_area=w*h

print(width,data)
print(w,h)
print(max_area)
