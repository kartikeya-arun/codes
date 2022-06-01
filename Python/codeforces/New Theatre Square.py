answer=[]
for t in range(int(input())):
    n,m,x,y=list(map(int,input().split()))
    y=min(y,2*x)
    ans=0
    for _ in range(n):
        i=0
        s=input() # Take a row as input as cost for each row can be calculated separately.
        while i<m:
            if s[i]=='*': # Move head as the tile is already paved.
                i+=1
                continue
            j=i
            if j+1<m and s[j+1]=='.': # Find the sequence of tiles to be paved.
                j+=1
            l=j-i+1 # find the length of '.' sequence.
            ans+=l%2*x+l//2*y #calculate the cost for current row and add to previously calculated cost
            i=j+1
    answer.append(str(ans))
print('\n'.join(answer))