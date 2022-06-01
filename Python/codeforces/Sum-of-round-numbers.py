t=int(input())
answerCount=[]
answerNums=[]
while t>0:
    num=input()
    if(int(num) in [0,1,2,3,4,5,6,7,8,9] or num[1:]=='0'*(len(num)-1)):
        answerCount.append(1)
        answerNums.append([num])
    else:
        terms=[]
        for i in range(len(num)):
            if(num[i]!="0"):
                term=int(num[i])*(10**(len(num)-1-i))
                terms.append(str(term))
        answerNums.append(terms)
        answerCount.append(len(terms))
    t-=1

for i in range(len(answerCount)):
    print(answerCount[i])
    print(' '.join(answerNums[i]))