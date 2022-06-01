t=int(input())
answer=[]
for i in range(t):
    a,b=list(map(int,input().split()))
    ans=b-(a%b) if a%b!=0 else 0
    answer.append(str(ans))

print('\n'.join(answer))