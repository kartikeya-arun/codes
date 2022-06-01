t=int(input())
answer=[]
while t>0:
    n=int(input())
    lst=list(map(int,input().split()))
    lst.sort()
    flag=False
    for i in range(1,n):
        if(lst[i]-lst[i-1]>1):
            flag=True

    answer.append("YES" if flag==False else "No")
    t-=1
print('\n'.join(answer))