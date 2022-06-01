n=int(input())
if n>=0:
    print(n)
else:
    a=int(n/10)
    b=int(n/100)*10-n%10
    print(max(a,b))

# if n>=0:
#     print(n)
# else:
#     n=str(n)
#     n=n[:len(n)-2]+str(min(int(n[len(n)-2]),int(n[len(n)-1])))
#     print(int(n))