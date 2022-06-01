answer=[]
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    o=[]
    e=[]
    for i in range(n):   # Greedy doesn't always mean sorting in reverse 
        if i%2 == 0 and a[i]%2!=0:
            e.append(i)
        if i%2==1 and a[i]%2!=1:
            o.append(i)
    if len(e)==len(o):
        answer.append(str(len(o)))
    else:
        answer.append(str(-1))
print('\n'.join(answer))    