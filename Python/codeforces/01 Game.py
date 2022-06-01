from typing import AnyStr


t=int(input())
answer=[]
while t>0:
    s=input()
    c0=0
    c1=0
    for i in s:
        if i=='0':
            c0+=1
        else:
            c1+=1
    if min(c0,c1)%2==1:
        answer.append('DA')
    else:
        answer.append('NET')
    t-=1

print('\n'.join(answer))