answer=[]
for i in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    s.sort()
    result=s[n-1]-s[0]
    for i in range(n):
        for j in range(i+1,n):
            result=min(result,s[j]-s[i])
    answer.append(str(result))
print('\n'.join(answer))