import math

answer=[]
for i in range(int(input())):
    n,m,k=list(map(int,input().split()))
    cards_in_hands=n//k
    if m<=cards_in_hands:
        answer.append(str(m))
    else:
        x=cards_in_hands
        y=math.ceil((m-x)/(k-1)) #important step (Greedy)
        answer.append(str(x-y))
print('\n'.join(answer))