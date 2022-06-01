n=int(input())
answer=''
for i in range(n):
    if(i%2==0):
        answer+='I hate '
        if(i==n-1):
            answer+='it'
        else:
            answer+='that '
    else:
        answer+='I love '
        if(i==n-1):
            answer+='it'
        else:
            answer+='that '

print(answer)