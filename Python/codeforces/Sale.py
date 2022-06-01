n,m=list(map(int,input().split()))
a=sorted(list(map(int,input().split())))
earning=0
for i in range(m):
    if a[i]<0:
        earning+=a[i]

print (abs(earning))