n,k=list(map(int,input().split()))

break_point=n//2 if n%2==0 else n//2+1

if k<=break_point:
    print (2*k-1)
else:
    print (2*(k-break_point))