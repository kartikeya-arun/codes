class Solution:
    def fib(self, n: int) -> int:
        # Bottom-up DP
        if n<2:
            return 1 if n==1 else 0
        fib=[0]*(n+1)
        fib[0]=0
        fib[1]=1
        for i in range(2,len(fib)):
            fib[i]=fib[i-1]+fib[i-2]
        return fib[n]
        
        # Top down DP
        # if n==0:
        #     return 0
        # if n==1:
        #     return 1
        # return self.fib(n-1)+self.fib(n-2)