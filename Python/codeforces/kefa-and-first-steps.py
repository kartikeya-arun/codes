n=int(input())
a=list(map(int,input().split()))
k=1
count=0
for i in range(1,n):
    if(a[i]>=a[i-1]):
        k+=1
    else:
        count=max(count,k)
        k=1
count=max(count,k)
print(count)