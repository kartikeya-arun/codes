n=int(input())
u={i for i in range(1,n+1)}       # Generating the set

def middleware(i,x,sum):
    set1=set()
    sumset=0
    while sumset<sum:             # middleware to handle if sum is divisible by n or n+1
        sumset+=x
        set1.add(x-i)
        if i>0:
            set1.add(i)
        i+=1
    return set1

if(n*(n+1)%4==0):                 # Sum of n natural numbers divided by 2 beacuse we have to find 2 sets
    sum=n*(n+1)/4 
    print('YES')
    if(sum%n==0):
        set1=middleware(0,n,sum)
    else:
        set1=middleware(1,n+1,sum)
    print(len(set1))
    print(' '.join(list(map(str,set1))))
    print(len(u)-len(set1))
    print(' '.join(list(map(str,u-set1))))
else:
    print('NO')