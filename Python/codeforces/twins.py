n=int(input())
coins=list(map(int,input().split()))
coins.sort()
balance=0
count=0
i=n-1
while balance<=sum(coins)/2:
    balance+=coins[i]
    count+=1
    i-=1

print(count)
