n,m=list(map(int,input().split()))
wordlist={}
answer=[]
for t in range(m):
    a,b=input().split()
    if len(b)<len(a):
        wordlist[a]=b
    else:
        wordlist[a]=a
lecture=input().split()
for word in lecture:
    answer.append(wordlist[word])

print(' '.join(answer))