n,m,a=list(map(int,input().split()))

answer=((m+a-1)//a)*((n+a-1)//a)
print(answer)