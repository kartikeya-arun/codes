k=int(input())
growth=sorted(list(map(int,input().split())),reverse=True)
months=0
i=0

while months<k and i<len(growth):
    months+=growth[i]
    i+=1

print(i) if months>=k else print(-1)