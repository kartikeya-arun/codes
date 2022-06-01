n,l=list(map(int,input().split()))
lanterns=list(map(int,input().split()))
lanterns.sort()
max_dist=0

for i in range(len(lanterns)-1):
    if abs(lanterns[i]-lanterns[i+1])>max_dist:
        max_dist=abs(lanterns[i]-lanterns[i+1])

d=max(max_dist/2,max(lanterns[0]-0,l-lanterns[n-1]))
print('%.10f'%d)