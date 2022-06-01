n=int(input())
answer="NO"
for i in range(1,n+1):
    if (set(str(i))=={'7','4'} or set(str(i))=={'4'} or set(str(i))=={'7'}) and n%i==0:
        answer="YES"
        break
print(answer)