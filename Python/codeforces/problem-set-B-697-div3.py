t=int(input())
answer=[]
for i in range(t):
    num=int(input())
    y=num%2020
    x=((num-y)/2020)-y
    if(x>=0 and y>=0):
        answer.append('yes')
    else:
        answer.append('no')

print('\n'.join(answer))