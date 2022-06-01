############################################ Find the contiguous subarray with largest sum #####s#################################### 

size=int(input())
a=list(map(int,input().split()))

max_so_far=a[0]
max_ending_here=0

for i in range(size):
    max_ending_here+=a[i]
    if max_ending_here<0:
        max_ending_here=0
    elif max_so_far<max_ending_here:
        max_so_far=max_ending_here

print(max_so_far) 