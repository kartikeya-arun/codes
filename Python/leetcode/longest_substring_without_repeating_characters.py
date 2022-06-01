class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=='':
            return 0
        maxL=1
        for i in range(len(s)-1):
            hashSet=set()
            hashSet.add(s[i])
            count=1
            while i+count<len(s) and s[i+count] not in hashSet:
                maxL=max(maxL,count+1)
                hashSet.add(s[i+count])
                count+=1
        return maxL