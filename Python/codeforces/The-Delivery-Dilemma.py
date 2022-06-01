t=int(input())
answer=''
for i in range(t):
    n=int(input())
    delivery_times=list(map(int,input().split()))
    pickup_times=list(map(int,input().split()))
    delivery_times.sort()
    pickup_times.sort()
    tdkmax=max(delivery_times)
    for i in range(n):
        if(delivery_times[i]>tdkmax):
            sum_pick+=pickup_times[i]
        else:
            
