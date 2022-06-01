n=int(input())
forces=[]
for i in range(n):
    force=list(map(int,input().split()))
    forces.append(force)

sumx=0
sumy=0
sumz=0
for i in range(n):
    sumx+=forces[i][0]
    sumy+=forces[i][1]
    sumz+=forces[i][2]

if (sumx,sumy,sumz)!=(0,0,0):
    print("NO")
else:
    print("YES")