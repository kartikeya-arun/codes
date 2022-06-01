n=int(input())
lst=list(map(int,input().split()))
answer=0
pre=lst[0]
for i in range(1,n):
    if(pre>lst[i]):
        answer+=pre-lst[i]
    else:
        pre=lst[i]

print(answer)