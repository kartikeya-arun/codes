answer=[]
for t in range(int(input())):
    n,k=list(map(int,input().split()))
    if n<k:
        answer.append(str(k-n))
    elif n%2==k%2:
        answer.append('0')
    else:
        answer.append('1')

print('\n'.join(answer))