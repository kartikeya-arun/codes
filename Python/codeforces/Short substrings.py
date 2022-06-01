t=int(input())
answer=[]
while t>0:
    b=input()
    a=''
    for i in range(len(b)):
        if(i%2==0):
            a+=b[i]
    answer.append(a+b[len(b)-1])
    t-=1

print('\n'.join(answer))