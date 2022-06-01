n=int(input())
passengers=[]
currentCount=0
for i in range(n):
    ai,bi=list(map(int,input().split()))
    currentCount-=ai
    currentCount+=bi
    passengers.append(currentCount)

print(max(passengers))