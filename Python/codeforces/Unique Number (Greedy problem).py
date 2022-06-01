answer=[]
for t in range(int(input())):
    n=int(input())
    digits=[9,8,7,6,5,4,3,2,1]
    if n>45:
        answer.append('-1')
    else:
        ans=[]
        i=0
        while n>digits[i]:
            n-=digits[i]
            ans.append(str(digits[i]))
            i+=1
        ans.append(str(n))
        ans=ans[::-1]
        answer.append(''.join(ans))

print('\n'.join(answer))