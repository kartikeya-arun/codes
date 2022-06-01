n,m=list(map,int(input().split()))
if m>n:
    print(-1)
else:
    if int(n/2)%m==0:
        print(int(n/2))
    else:
        print (int(n/2)+int(n/2)%m)