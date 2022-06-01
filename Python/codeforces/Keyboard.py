r1='qwertyuiop'
r2='asdfghjkl;'
r3='zxcvbnm,./'
rowLen=len(r1)

dir=input()
text=list(input())
if dir=='R':
    for i in range(len(text)):
        if text[i] in r1:
            text[i]=r1[r1.index(text[i])-1]
        elif text[i] in r2:
            text[i]=r2[r2.index(text[i])-1]
        elif text[i] in r3:
            text[i]=r3[r3.index(text[i])-1]
else:
    for i in range(len(text)):
        if text[i] in r1:
            text[i]=r1[r1.index(text[i])+1]
        if text[i] in r2:
            text[i]=r2[r2.index(text[i])+1]
        if text[i] in r3:
            text[i]=r3[r3.index(text[i])+1]

print(''.join(text))