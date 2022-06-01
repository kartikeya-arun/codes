n1=input()
n2=int(input(),2)
answer=bin(int(n1,2)^n2)[2:]
print('0'*(len(n1)-len(answer))+answer)