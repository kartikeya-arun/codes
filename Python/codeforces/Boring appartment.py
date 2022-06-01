answer=[]
for t in range(int(input())):
    n=input()
    ans=(int(n[0])-1)*10+(len(n)*((len(n)+1)/2))
    answer.append(str(int(ans)))
print('\n'.join(answer))