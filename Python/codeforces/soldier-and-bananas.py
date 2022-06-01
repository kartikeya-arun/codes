k,w,n=list(map(int,input().split()))
cost=k
for i in range(2,n+1):
    cost+=i*k

if(cost-w<=0):
    print(0)
else:
    print(cost-w)