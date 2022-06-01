string=input().lower()
vowels={'a','o','y','e','u','i'}
answer=''
for i in string:
    if i not in vowels:
        answer+='.'+i
print(answer)