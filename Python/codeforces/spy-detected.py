t=int(input())
answer=[]
for i in range(t):
    d={}
    n=int(input())
    lst=list(map(int,input().split()))
    for i in lst:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    
    for i in d.keys():
        if d[i]==1:
            answer.append(str(lst.index(i)+1))
            break

print('\n'.join(answer))