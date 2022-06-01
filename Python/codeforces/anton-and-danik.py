n=int(input())
scorecard=input()
# anton=0
# danik=0
# for i in scorecard:
#     if i=='A':
#         anton+=1
#     else:
#         danik+=1

# if(anton>danik):
#     print('Anton')
# elif(danik>anton):
#     print('Danik')
# else:
#     print('Friendship')

winner=0
for i in scorecard:
    if i=='A':
        winner+=1
    else:
        winner-=1

if(winner>0):
    print('Anton')
elif(winner<0):
    print('Danik')
else:
    print('Friendship')