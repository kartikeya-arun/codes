class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        env=sorted(envelopes,key=lambda x:(x[0],-x[1]))
        dp=[]
        
        for w,h in env:
            # i,N=0,len(dp)             Dynamic programming : TLE
            # while i<N:
            #     if h<=dp[i]:break
            #     i+=1
            i=bisect_left(dp,h)        # Binary search: Accepted
            # if i==N:
            if i==len(dp):
                dp.append(h)
            else:
                dp[i]=h
        return len(dp)