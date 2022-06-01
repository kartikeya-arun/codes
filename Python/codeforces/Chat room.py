message=input()
b='hello'
j=0
count=0
for i in message:
    if i==b[j]:
        j+=1
        count+=1
        if count==5:
            break

print('YES') if count==5 else print('NO')