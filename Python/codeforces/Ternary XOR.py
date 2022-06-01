t=int(input())
answer=[]
while t>0:
    n=int(input())
    x=list(input())
    a=['0']*n
    b=['0']*n

    # Let's iterate from left to right over the digits of x.
    
    for i in range(n):

        # And if the current digit x[i] is 1 then the optimal choise is to set a[i]=1 and b[i]=0.
        # What happens after the first occurrence of 1?
        
        if x[i]=='1':
            a[i]='1'
            b[i]='0'

            # Because of this choice a is greater than b even if all remaining digits in b are 2.
            # So for each j>i set a[j]=0 and b[j]=x[j] and print the answer.
            # The case without 1 is even easier and in fact we handle it automatically.

            for j in range(i+1,n):
                b[j]=str(x[j])
            break
        else:
            
            # If the current digit is either 0 or 2 then we can set a[i]=b[i]=0 or a[i]=b[i]=1 correspondingly.
            # There are no better choices.
            
            if x[i]=='0':
                a[i]='0'
                b[i]='0'
            elif x[i]=='2':
                a[i]='1'
                b[i]='1'
    answer.append(''.join(a))
    answer.append(''.join(b))
    t-=1
print('\n'.join(answer))