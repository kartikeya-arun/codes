mishka=0
chris=0
for t in range(int(input())):
    dicem,dicec=list(map(int,input().split()))
    if dicem>dicec:
        mishka+=1
    elif dicec>dicem:
        chris+=1
if (mishka>chris):
    print('Mishka')
elif (chris>mishka):
    print('Chris')
else:
    print('Friendship is magic!^^')