answer=[]
for t in range(int(input())):
    x,y=list(map(int,input().split()))
    a,b=list(map(int,input().split()))
    b=min(b,a+a)
    if x<y:
        x,y=y,x
    answer.append(str(y*b+(x-y)*a))
print('\n'.join(answer))