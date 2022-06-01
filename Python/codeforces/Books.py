n,t=list(map(int,input().split()))
a=list(map(int,input().split()))
a.sort()
count=0
time_taken=0
for i in range(n):
    if t-time_taken<a[i]:
        break
    else:
        count+=1
        time_taken+=a[i]
print(count)