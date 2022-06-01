# Enter your code here. Read input from STDIN. Print output to STDOUT
# from collections import Counter
# k=int(input())
# rno=list(map(int,input().split()))
# c=Counter(rno)
# for i in rno:
#     if(c[i]<k):
#         print (i)
k=int(input())
rno=list(map(int,input().split()))
setRno=set(rno)
print(((sum(setRno)*k)-(sum(rno)))//(k-1))