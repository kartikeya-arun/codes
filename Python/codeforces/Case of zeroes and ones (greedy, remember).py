n=int(input())
string=input()
count0=0
count1=0
for i in range(n):
    if string[i]=='1':
        count0+=1
    else:
        count1+=1

answer=count0+count1-(2*min(count0,count1))
print(answer)