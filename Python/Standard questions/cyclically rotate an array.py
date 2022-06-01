n=int(input())
a=list(map(int,input().split()))

first=a.pop(n-1)

print([first]+a)
