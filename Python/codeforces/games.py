n=int(input())
a=[0]*n
h=[0]*n
for i in range(n):
    a[i],h[i]=list(map(int,input().split()))

count=0
for i in range(n):
    for j in range(n):
        if i!=j and h[i]==a[j]:
            count+=1

print(count)