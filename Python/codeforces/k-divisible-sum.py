t=int(input())
answer=[]

for i in range(t):
    n,k=list(map(int,input().split()))
    cf=(n+k-1)//k
    answer.append(str((cf*k+n-1)//n))

print('\n'.join(answer))