m,s=list(map(int,input().split()))
minn=[]
maxx=[]

if s==0:
    if m==1:
        print('0 0')
    else:
        print('-1 -1')
else:
    for i in range(m):
        k=min(9,s)
        maxx.append(str(k))
        s-=k

    if s>0:
        print('-1 -1')
    else:
        minn=maxx[::-1]
        j=0
        while minn[j]=='0':
            j+=1
        minn[0]=str(int(minn[0])+1)
        minn[j]=str(int(minn[j])-1)
        print(''.join(minn),''.join(maxx))