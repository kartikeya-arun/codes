t=int(input())
answer=[]
while t>0:
    n=int(input())
    count2=0
    count3=0
    while n%2==0:
        n//=2
        count2+=1

    while n%3==0:
        n//=3
        count3+=1

    if n==1 and count2<=count3:
        answer.append(str(2*count3-count2))
    else:
        answer.append(str(-1))
    
    # TOO SLOW
    # moves=0
    # n=int(input())
    # while n!=1:
    #     if n%3!=0:
    #         moves=-1
    #         break
    #     elif n%6==0:
    #         n//=6
    #     else:
    #         n*=2
    #     moves+=1
    # answer.append(str(moves))
    t-=1

print('\n'.join(answer))