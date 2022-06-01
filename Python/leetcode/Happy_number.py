class Solution:
    def isHappy(self, n: int) -> bool:
        # visited=set()
        # while n not in visited:
        #     visited.add(n)
        #     n=self.sumOfDigits(n)
        #     if n==1:
        #         return True
        # return False
        
        slow=n
        fast=self.sumOfDigits(n)
        while fast!=1 and slow!=fast:
            slow=self.sumOfDigits(slow)
            fast=self.sumOfDigits(self.sumOfDigits(fast))
        return fast==1
    
    def sumOfDigits(self,n):
        return sum([int(d)**2 for d in str(n)])