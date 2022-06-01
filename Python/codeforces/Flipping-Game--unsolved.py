n=int(input())
seq=list(map(int,input().split()))
subseq=[]
for i in seq:
    if i==1:
        subseq.append(-1)
    else:
        subseq.append(1)

max_so_far=subseq[0]
max_ending_here=0

for i in range(n):
    max_ending_here+=subseq[i]
    if max_ending_here<0:
        max_ending_here=0
    elif max_so_far<max_ending_here:
        max_so_far=max_ending_here

print (max_so_far)