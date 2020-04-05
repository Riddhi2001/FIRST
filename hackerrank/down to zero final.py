Q = int(input())
A = 0

for i in range(Q):
    N = int(input())
    factors=[]
    count = 0
    while N != 0:
        factors.clear()
        for i in range(1,N):
            
            if N%i==0:
                factors.append(i)
                print(factors)
        try:    
            A = max(factors)
        except:
            pass
        print('max factor',A)
        print('original N',N)
        if len(factors)==1:
            N -= 1
        elif A<N-1:
            N = A
        else :
            N -= 1
        print('new N',N)
        if N !=0:
            count += 1
    print(count)





