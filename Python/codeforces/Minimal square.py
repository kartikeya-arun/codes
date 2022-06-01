answer=[]
for i in range(int(input())):
    a,b=list(map(int,input().split()))
    if min(a,b)*2 >=max(a,b):
        answer.append(str((min(a,b)*2)**2))
    else:
        answer.append(str((max(a,b))**2))
print('\n'.join(answer))