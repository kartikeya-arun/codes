answer=[]
for t in range(int(input())):
    n=int(input())
    if n%2==0:
        answer.append(str(int(n/2)))
    else:
        answer.append(str(int(n/2)+1))
print('\n'.join(answer))