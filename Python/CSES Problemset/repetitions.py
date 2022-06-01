s=input()
ptr=s[0]
count=0
maxlen=0
for i in s:
    if ptr!=i:
        ptr=i
        count=1
    else:
        count+=1
        if count>maxlen:
            maxlen=count
print(maxlen)