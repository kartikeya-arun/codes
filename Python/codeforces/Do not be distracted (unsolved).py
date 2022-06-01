import string

answer=[]
for t in range(int(input())):
    n=int(input())
    s=input()
    for c in string.ascii_uppercase:
        first=n
        last=-1
        for i in range(n):
            if s[i] == c:
                first=min(first,i)
                last=max(last,i)
        for i in range(first,last):
            if s[i]!=c:
                answer.append('NO')
                break
    answer.append('YES')
print('\n'.join(answer))