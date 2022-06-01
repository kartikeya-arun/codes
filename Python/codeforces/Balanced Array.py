t=int(input())
answer=[]
while t>0:
    n=int(input())
    even=[]
    odd=[]
    if n%4!=0:
        answer.append('NO')
    else:
        for i in range(2,n+1,2):
            even.append(i)
        for i in range(1,n,2):
            odd.append(i)
        odd[(n//2)-1]+=n//2
        answer.append("YES")
        answer.append(' '.join(list(map(str,(even+odd)))))
    t-=1
print('\n'.join(answer))