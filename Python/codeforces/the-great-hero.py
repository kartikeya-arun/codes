from math import ceil

test=int(input())
answer=[]
for i in range(test):
    A,B,n=list(map(int,input().split()))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    # answer.append(solution(A,B,n,a,b))
    damage=0
    for i in range(n):
        damage+=(ceil(b[i]/A))*a[i]
    if(B-damage+a[n-1]>=0):
        answer.append('YES')
    else:
        answer.append('NO')
 
print('\n'.join(answer))
# print(answer)