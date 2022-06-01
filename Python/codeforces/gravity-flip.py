n=int(input())
cubes=list(map(int,input().split()))
cubes.sort()
for i in range(len(cubes)):
    print(cubes[i],end=' ')