n,h=list(map(int,input().split()))
kids=list(map(int,input().split()))
bentkid=0
for i in kids:
    if i>h:
        bentkid+=1

print(len(kids)+bentkid)