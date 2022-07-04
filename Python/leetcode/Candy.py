class Solution:
    def candy(self, ratings: List[int]) -> int:
        N=len(ratings)
        q=deque()
        outdegree=[0]*N
        for i in range(N):
            if i-1>=0 and ratings[i]>ratings[i-1]:
                outdegree[i]+=1
            if i+1<N and ratings[i]>ratings[i+1]:
                outdegree[i]+=1
            if outdegree[i]==0:
                q.append(i)
        ans=[None]*N
        while len(q):
            cur=q.popleft()
            
            ans[cur]=1
            if cur-1>=0 and ratings[cur]>ratings[cur-1]:
                ans[cur]=max(ans[cur],ans[cur-1]+1)
            if cur+1<N and ratings[cur]>ratings[cur+1]:
                ans[cur]=max(ans[cur],ans[cur+1]+1)
            
            if cur-1>=0 and ratings[cur]<ratings[cur-1]:
                outdegree[cur-1]-=1
                
                if outdegree[cur-1]==0:
                    q.append(cur-1)
            if cur+1<N and ratings[cur]<ratings[cur+1]:
                outdegree[cur+1]-=1
                if outdegree[cur+1]==0:
                    q.append(cur+1)
        return sum(ans)