R, C =  map(int, input().split())
a = [] 
for i in range(0,R):                                                        #if u input 2 2
    a.append(str(input()))                                            # 10
                                                                                        # 11
print(a)    #prints (10,11)
for j in range(0,R):
    a[j] = list(a[j])
print(a)        #prints((1,0),(1,1))
print(a[0][0])  #prints 1
