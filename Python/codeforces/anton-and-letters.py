ip=input()
count={}
for i in ip:
    if i.isalpha():
        if i in count.keys():
            count[i]+=1
        else:
            count[i]=1

print(len(count.keys()))