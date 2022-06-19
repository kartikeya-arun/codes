class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # Binary Search
        # products.sort()
        # ans=[]
        # prefix=''
        # for c in searchWord:
        #     prefix+=c
        #     start=bisect.bisect_left(products,prefix)
        #     ans.append([w for w in products[start:start+3] if w.startswith(prefix)])
        # return ans
        
        # Two pointer
        products.sort()
        l,r=0,len(products)-1
        ans=[]
        for i in range(len(searchWord)):
            c=searchWord[i]
            while l<=r and (len(products[l])<=i or c!=products[l][i]):
                l+=1
            while l<=r and (len(products[r])<=i or c!=products[r][i]):
                r-=1
            ans.append([])
            rem=r-l+1
            for j in range(min(3,rem)):
                ans[-1].append(products[l+j])
        return ans