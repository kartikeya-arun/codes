n=int(input())
a=list(map(int,input().split()))
m=int(input())
q=list(map(int,input().split()))
answer=[]
for i in range(1,n):
    a[i]+=a[i-1]

arr=[]
for i in range(n):
    arr+=[i+1]*a[i]
print (arr)
print (a)
for i in q:
    print(arr[i])