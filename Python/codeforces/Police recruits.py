n=int(input())
events=list(map(int,input().split()))
police=0
unnoticed=0
for i in events:
    if i>0:
        police+=i
    else:
        if police>0:
            police-=1
        else:
            unnoticed+=1
print(unnoticed)