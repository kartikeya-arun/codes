k,n=list(map(int,input().split()))
arr=list(map(int,input().split()))
arr.sort()
answer=arr[n-1]-arr[0]
for i in range(1,n):
    if arr[i]>k:
        maxT=max(arr[i-1]+k,arr[n-1]-k)
        minT=min(arr[i]-k,arr[0]+k)
        answer=min(answer,maxT-minT)
print(answer)