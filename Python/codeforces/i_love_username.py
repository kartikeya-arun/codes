n=int(input())
scores=list(map(int,input().split()))
prev=[scores[0]]
awesome=0
for i in range(1,len(scores)):
    if(scores[i]>max(prev)):
        awesome+=1
    if(scores[i]<min(prev)):
        awesome+=1
    prev.append(scores[i])

print(awesome)