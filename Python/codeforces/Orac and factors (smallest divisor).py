for t in range(int(input())):
    n,k=list(map(int,input().split()))
    if n%2==0:
        print(n+2*k)
    else:
        dn=0
        for i in range(n,2,-1):
            if n%i==0:
                dn=i
        print(dn+n+2*(k-1))    