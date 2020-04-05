Q = int(input())
A = 0
count = 1
for i in range(Q):
    N = int(input())
    factors=[]
    while N != 0:
        for i in range(1,N):
            if N%i==0:
                factors.append(i)
            A = max(factors)
        if A< N-1:
            N = A
        else:
            N -=1
        count += 1
    print(count)

