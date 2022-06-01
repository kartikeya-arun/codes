n,m=list(map(int,input().split()))

if min(n,m)%2!=0:
    print("Akshat")
else:
    print("Malvika")

# One-Liner
# print("Akshat") if min(list(map(int,input().split())))%2!=0 else print("Malvika")