n=int(input())
s=input()
# res = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if len(s[i:j]) == 2]
d={}
for i in range(n):
    for j in range(i+1,n+1):
        if len(s[i:j])==2:
            if s[i:j] in d.keys():
                d[s[i:j]]+=1
            else:
                d[s[i:j]]=1
# for i in res:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
print(list(d.keys())[list(d.values()).index(max(d.values()))])