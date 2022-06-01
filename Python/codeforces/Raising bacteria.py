x=int(input())
bacteria=0
i=1
while x>0:
    if x&1:
        bacteria+=1
    x>>=1
print(bacteria)