class Solution:
    def climbStairs(self, n: int) -> int:
        last,secondLast=1,1
        for i in range(n-2,-1,-1):
            last,secondLast=secondLast,last+secondLast
        return secondLast
        
        # if n<3:
        #     return n
        # n1=1
        # n2=2
        # for i in range(1,n):
        #     n1,n2=n2,n1+n2
        # return n1