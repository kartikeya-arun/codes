from typing import Counter


n=int(input())
s=list(map(int,input().split()))
total=s.count(4)+s.count(3)+int(s.count(2)/2)
count1=s.count(1)
count1-=s.count(3)
if (s.count(2)%2==1):
    total+=1
    count1-=2
if count1>0:
    total+=int((count1+3)/4)

print(total)
