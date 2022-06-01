answer=[]
for i in range(int(input())):
    n=int(input())
    s=input()
    bal=0
    ans=0
    for i in range(n):
        if s[i]=='(':
            bal+=1
        elif s[i]==')':
            bal-=1
        if bal<0:
            ans+=1
            bal+=1
    answer.append(str(ans))
print('\n'.join(answer))