word=input()

if word[0].islower():
    caps=True
    for i in word[1:]:
        if i.islower():
            caps=False
            break

    print(word) if caps==False else print(word.capitalize())
else:
    caps=True
    for i in word[1:]:
        if i.islower():
            caps=False
            break
    print(word) if caps==False else print(word.lower())