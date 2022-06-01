from math import floor
n,m,a,b=list(map(int,input().split()))
cost=0
if m*a<=b:
    cost=n*a
else:
    cost=(n//m)*b + min((n%m)*a,b)

print(cost)