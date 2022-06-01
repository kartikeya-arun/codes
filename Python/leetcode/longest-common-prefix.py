class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # pre=''
        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if i==len(s) or s[i]!=strs[0][i]:
        #             return pre
        #     pre+=strs[0][i]
        # return pre
        
        if strs==None or len(strs)==0:
            return ''
        minLen=float('inf')
        for s in strs:
            minLen=min(minLen,len(s))
        low=1
        high=minLen
        while low<=high:
            mid=(low+high)//2
            if self.isCommonPrefix(strs,mid):
                low=mid+1
            else:
                high=mid-1
        return strs[0][:(low+high)//2]
    
    def isCommonPrefix(self,strs,size):
        str1=strs[0][:size]
        for i in range(1,len(strs)):
            if not strs[i].startswith(str1):
                return False
        return True