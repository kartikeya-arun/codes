s,n=list(map(int,input().split()))
win=True
dragons=[]
for i in range(n):
    (x,y)=list(map(int,input().split()))
    dragons.append((x,y))

dragons.sort()
for i in range(n):
    if s<=dragons[i][0]:
        win=False
        break
    else:
        s+=dragons[i][1]

print('YES') if win==True else print('NO')