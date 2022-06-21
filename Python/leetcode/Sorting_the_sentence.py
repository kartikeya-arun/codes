class Solution:
    def sortSentence(self, s: str) -> str:
        # s=s.split(' ')
        # ans=[None]*len(s)
        # for i in s:
        #     ans[int(i[-1])-1]=i[:-1]
        # return ' '.join(ans)
        
        # Shorter
        k=sorted(s.split(),key=lambda x:x[-1])
        return ' '.join(j[:-1] for j in k)