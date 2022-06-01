#!/bin/python3
n=int(input())

lst=[]
odd=[]
even=[]

for i in range(n):
    lst.append(i+1)

for i in lst:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)

if(len(odd+even)==1):
    complete=odd+even
    print(complete[0])
elif(abs(odd[-1]-even[0])<=1 and abs(even[-1]-odd[0])<=1):
    print('NO SOLUTION')
elif(abs(odd[-1]-even[0])<=1):
    complete=list(map(str,even+odd))
    answer=' '.join(complete)
    print(answer)
else:
    complete=list(map(str,odd+even))
    answer=' '.join(complete)
    print(answer)
    