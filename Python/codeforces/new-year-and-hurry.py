total_time=4*60
n,k=list(map(int,input().split()))
time_for_contest=total_time-k
solvable_problems=0
i=1
while time_for_contest>=5*i and i<=n:
    solvable_problems+=1
    time_for_contest-=5*i
    i+=1

print(solvable_problems)