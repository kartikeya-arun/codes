n=int(input())
group=1
prev=''
for i in range(n):
    ip=input()
    if ip==prev or prev=='':
        prev=ip
    else:
        group+=1
        prev=ip
print(group)