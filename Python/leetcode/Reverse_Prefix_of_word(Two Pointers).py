class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # if ch in word:
        #     beg,end=word.split(ch,1)
        #     return ch+beg[::-1]+end
        # else:
        #     return word
        
        wordLst=list(word)
        l,r=0,0
        while r<len(wordLst) and l<=r:
            if wordLst[r]==ch:
                while r<len(wordLst) and l<=r:
                    wordLst[l],wordLst[r]=wordLst[r],wordLst[l]
                    l,r=l+1,r-1
                return ''.join(wordLst)
            r+=1
        return word