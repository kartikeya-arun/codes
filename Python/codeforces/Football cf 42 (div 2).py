d={}
for t in range(int(input())):
    goal=input()
    if goal in d.keys():
        d[goal]+=1
    else:
        d[goal]=1

winner=max(d,key=d.get)
print(winner)
