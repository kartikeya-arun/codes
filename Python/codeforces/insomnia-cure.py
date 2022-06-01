from math import gcd
def lcm(a,b):
    return abs(a*b)//gcd(a,b)

k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())

N1=d//k+d//l+d//m+d//n
N2=d//lcm(k,l)+d//lcm(l,m)+d//lcm(m,n)+d//lcm(k,m)+d//lcm(k,n)+d//lcm(l,n)
N3=d//lcm(lcm(k,l),m)+d//lcm(lcm(l,m),n)+d//lcm(k,lcm(m,n))+d//lcm(k,lcm(l,n))
N4=d//lcm(k,lcm(l,lcm(m,n)))

print(N1-N2+N3-N4)