answer=[]
for i in range(int(input())):
    x,y,n=list(map(int,input().split()))
    if n-n%x+y<=n:
        answer.append(str(n-n%x+y))
    else:
        answer.append(str(n-n%x-(x-y)))
    
print('\n'.join(answer))