a=int(input())
b=int(input())
c=int(input())
answer=0
answer=max(answer,(a+b)*c)
answer=max(answer,a+b*c)
answer=max(answer,a*b+c)
answer=max(answer,a*b*c)
answer=max(answer,a*(b+c))
answer=max(answer,a+b+c)

print (answer)