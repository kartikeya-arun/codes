from collections import Counter

nums=[3,0,1,0]
k=1

count=Counter(nums)
print(count)
freq=[[] for i in range(len(nums)+1)]

for n,c in count.items():
    print(freq[c])
    print(n,c)
    freq[c].append(n)
    print(freq[c])
    
print(freq)    
ans=[]
for i in range(len(freq)-1,0,-1):
    for n in freq[i]:
        ans.append(n)
        if len(ans)==k:
            print(ans)