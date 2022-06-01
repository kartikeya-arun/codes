# class Solution:
#     def reverseWords(self, s: str) -> str:
#         s=s.split(' ')
#         for i in s:
#             i=i.split()
#             low=0
#             high=len(i)-1
#             while low<high:
#                 i[low],i[high]=i[high],i[low]
#                 low+=1
#                 high-=1
#             i=''.join(i)
#         return s

s=input()
s=s.split(' ')
for i in range(len(s)):
    s[i]=s[i][::-1]
    # i=i.split()
    # low=0
    # high=len(i)-1
    # while low<high:
    #     i[low],i[high]=i[high],i[low]
    #     low+=1
    #     high-=1
    # i=''.join(i)
print(' '.join(s))