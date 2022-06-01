n,m=list(map(int,input().split()))
puzzles=sorted(list(map(int,input().split())))
mindiff=max(puzzles[:n])-min(puzzles[:n])
for i in range(m-n+1):
    diff=max(puzzles[i:i+n])-min(puzzles[i:i+n])
    if diff<mindiff:
        mindiff=diff

print(mindiff)
