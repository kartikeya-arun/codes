n=int(input())
welfare=sorted(list(map(int,input().split())))
max=welfare[n-1]
total_expenditure=0
for i in range(n):
    total_expenditure+=max-welfare[i]
print(total_expenditure)