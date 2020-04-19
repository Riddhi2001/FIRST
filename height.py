t=int(input())
for i in range(t):
    peak=0
    n=int(input())
    height=[int(i) for i in input().split()]
    for i in range(1,n):
        if height[i] > height[i-1] and height[i] > height[i+1]:
            peak += 1
    print(peak)
        
