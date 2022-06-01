for t in range(int(input())):
    s=int(input())
    ans=0
    while s>0:
        if s<10:
            ans+=s
            s=0
        else:
            n=int(s/10)
            ans+=n*10
            s%=10
            s+=n
    print(int(ans))