# import re

formation=input()
count1=0
count0=0
for i in formation:
    if i=='1':
        count1+=1
        count0=0
        if count1==7:
            print('YES')
            break
    elif i=='0':
        count0+=1
        count1=0
        if count0==7:
            print('YES')
            break
else:
    print('NO')

# if re.search("1{7}|0{7}",formation):
#     print('YES')
# else:
#     print('NO')