test=int(input())
answer=[]
while test!=0:
    n,k=list(map(int,input().split()))
    h=list(map(int,input().split()))
    max_element=max(h)
    if(n*max_element<k):
        answer.append(-1)
        continue

    ans=n+1
    for j in range(k):
        pos=-2
        for i in range(n-1):
            if h[i]<h[i+1]:
                h[i]+=1
                pos=i
                break
        ans=pos+1
        if(pos==-2):
            break
        h[pos]+=1
    answer.append(ans)
    test-=1

print(answer)
