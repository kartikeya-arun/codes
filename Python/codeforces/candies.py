t=int(input())
answer=[]
while t>0:
    n=int(input())
    for i in range(2,30):
        if n%(2**i-1)==0:
            x=n//(2**i-1)
            break
    answer.append(str(x))
    t-=1

print('\n'.join(answer))