test=int(input())
answer=[]
for i in range(test):
    string=input()
    ans=''
    for i in range(len(string)):
        if i%2==0:
            ans+='a' if (string[i]!='a') else 'b'
        else:
            ans+='z'if(string[i]!='z') else 'y'
    answer.append(ans)
print('\n'.join(answer))