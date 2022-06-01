answer=[]
for i in range(int(input())):
    n=int(input())
    big=2**n
    small=0
    for i in range(int(n/2)):
        big+=2**i
    for i in range(int(n/2),n):
        small+=2**i
    answer.append(str((big-small)-1))
print('\n'.join(answer))