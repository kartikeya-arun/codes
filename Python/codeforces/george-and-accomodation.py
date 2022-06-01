n=int(input())
availableRooms=0
for i in range(n):
    pi,qi=list(map(int,input().split()))
    if qi-pi>=2:
        availableRooms+=1

print(availableRooms)