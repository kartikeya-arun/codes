n,m=list(map(int,input().split()))
flag=0
for i in range(n):
    if(i%2==0):
        print('#'*m)
    elif (flag==0):
        print('.'*(m-1)+'#')
        flag=1
    else:
        print('#'+'.'*(m-1))
        flag=0