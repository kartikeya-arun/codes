class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans=[]
        prefix=''
        for c in searchWord:
            prefix+=c
            start=bisect.bisect_left(products,prefix)
            ans.append([w for w in products[start:start+3] if w.startswith(prefix)])
        return ans