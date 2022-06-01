n=int(input())
answer=[]
if n%2==0:
    for i in range(n//2):
        answer.append('2')
else:
    for i in range((n//2)-1):
        answer.append('2')
    answer.append('3')

print(len(answer))
print(' '.join(answer))