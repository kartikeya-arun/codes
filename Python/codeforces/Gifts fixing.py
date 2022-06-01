answer=[]
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=0
    for i in range(n):
        ans+=max(a[i]-min(a),b[i]-min(b)) # <-- smart solution
    answer.append(str(ans))
print('\n'.join(answer))