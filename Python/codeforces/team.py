n=int(input())
answer=0
for i in range(n):
    ip=list(map(int,input().split()))
    if(sum(ip)>1):
        answer+=1
print (answer)