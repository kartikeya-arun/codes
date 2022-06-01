answer=[]
for t in range(int(input())):
    n=int(input())
    s=input()
    ans=0
    sortedS=sorted(s)
    for i in range(n):
        if s[i]!=sortedS[i]:
            ans+=1
    answer.append(str(ans))
print('\n'.join(answer))