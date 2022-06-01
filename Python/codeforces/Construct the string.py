t=int(input())
answer=[]
while t>0:
    n,a,b=list(map(int,input().split()))
    char=''
    for i in range(n):
        char+=chr(ord('a')+i%b)
    answer.append(char)
    t-=1
print('\n'.join(answer))