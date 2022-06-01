answer=[]
for i in range(int(input())):
    n,k=list(map(int,input().split()))
    a=sorted(list(map(int,input().split())))
    b=list(map(int,input().split()))
    b.sort(reverse=True)
    ans=0
    for i in range(n):
        if i<k:
            ans+=max(a[i],b[i])
        else:
            ans+=a[i]
        
    answer.append(str(ans))

print('\n'.join(answer))