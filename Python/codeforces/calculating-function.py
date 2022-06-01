n=int(input())

if(n%2==0):
    answer=n//2
else:
    answer=-(n+1)//2

# answer=0
# for i in range(1,n+1):
#     answer+=(-1)**i*i

print(answer)