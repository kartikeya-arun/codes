class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
#         for i in range(len(prices)-1):
#             j=min(len(prices)-1,i+1)
#             while j>i and j<len(prices) and prices[j]>prices[i]:
#                 j+=1
#             if j<len(prices) and prices[j]<prices[i]:
#                 prices[i]=prices[i]-prices[j]
#         return prices
        
        ans=prices.copy()
        stack=[]
        for i in range(len(prices)):
            while len(stack)!=0 and prices[stack[-1]]>=prices[i]:
                ans[stack[-1]]=prices[stack[-1]]-prices[i]
                stack.pop()
            stack.append(i)
        return ans