n,k=map(int,input().split())
scores=list(map(int,input().split()))
answer=0
for i in scores:
    if(i>0 and i>=scores[k-1]):
        answer+=1

print (answer)