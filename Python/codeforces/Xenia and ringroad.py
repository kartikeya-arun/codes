n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
time=0
loc=1
for i in range(m):
    if loc<=a[i]:
        time+=a[i]-loc
    else:
        time+=n-loc+a[i]
    loc=a[i]
print(time)