class Solution:
    def tribonacci(self, n: int) -> int:
        # Bottom-up DP
        # if n==0:
        #     return 0
        # if n==1:
        #     return 1
        # if n==2:
        #     return 1
        # t=[0]*(n+1)
        # t[0]=0
        # t[1]=1
        # t[2]=1
        # for i in range(3,len(t)):
        #     t[i]=t[i-1]+t[i-2]+t[i-3]
        # return t[n]
    
        # Optimal solution - constant space since only previous 3  values are required to calculate the next value
        n0,n1,n2=0,1,1
        for i in range(n):
            n0,n1,n2=n1,n2,n0+n1+n2
        return n0