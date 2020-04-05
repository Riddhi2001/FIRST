Q =27#int(input())
A = 0
listofN = [3,34,86,73,40,73,87,57,81,32,83,39,98,89,86,44,29,36,53,44,72,31,88,48,17,62,11]
answers = [3,6,7,6,5,5,8,6,5,5,7,6,7,8,7,7,7,5,7,7,5,6,7,5,5,7,6]
for i in range(Q):
    N = listofN[i]#int(input())
    print(N)
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
        #if N !=0:
        count += 1
    print(count)
    if(count == answers[i]):
        print('correct')
    else:
        print('incorrect')
    print('----')

