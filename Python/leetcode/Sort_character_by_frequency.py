class Solution:
    def frequencySort(self, s: str) -> str:
        # c=Counter(s)
        # c=sorted(c.items(),key=lambda x:-x[1])
        # ans=''
        # for k,v in c:
        #     ans+=k*v
        # return ans
        c=Counter(s).most_common()
        return ''.join([k*v for k,v in c])