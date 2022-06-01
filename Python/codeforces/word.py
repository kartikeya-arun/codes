word=input()
count=0
for i in word:
    if i.islower():
        count+=1
    elif i.isupper():
        count-=1

if count>0:
    print(word.lower())
elif count<0:
    print(word.upper())
else:
    print(word.lower())