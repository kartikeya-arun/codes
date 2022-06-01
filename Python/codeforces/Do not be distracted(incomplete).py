answer=[]
for t in range(int(input())):
    n=int(input())
    seen=[]
    s=input()
    sus=0
    for i in range(n):
        if s[i] in seen:
            answer.append('NO')
            sus=1
            break
        else:
            seen.append(s[i])
    if sus==0:
        answer.append('YES')
print('\n'.join(answer))