n=int(input())
p=list(map(int,input().split()))
answer=[0]*n
for i in range(n):
    answer[p[i]-1]=i+1

print(' '.join(list(map(str,answer))))