n=int(input())
while(n!=1):
    if(n%2==0):
        print(int(n),end=' ')
        n=n/2
    else:
        print(int(n),end=' ')
        n=n*3+1
print(int(n))