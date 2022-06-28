class Solution:
    def minDeletions(self, s: str) -> int:
        counts=[0]*26
        for i in s:
            counts[ord(i)-ord('a')]+=1
        seen=set()
        delCount=0
        for i in range(26):
            while counts[i] and counts[i] in seen:
                counts[i]-=1
                delCount+=1
            seen.add(counts[i])
        return delCount