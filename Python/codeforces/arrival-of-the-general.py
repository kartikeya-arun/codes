n=int(input())
soldiers=list(map(int,input().split()))
tallest=max(soldiers)
shortest=min(soldiers)
index_tall=soldiers.index(tallest)
index_short=n-1-soldiers[::-1].index(shortest)

answer=index_tall-1+n-index_short

if(index_tall>index_short):
    answer-=1
print(answer)
