k,r=list(map(int,input().split()))
for i in range(1,10):
    if (k*i)%10==0 or (k*i)%10==r:
        print(i)
        break