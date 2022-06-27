class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Binary search
        # r,c=len(grid),len(grid[0])
        # def binSearch(row,l,r):
        #     while l<=r:
        #         m=(l+r)//2
        #         if grid[row][m]>=0:
        #             l=m+1
        #         else: r=m-1
        #     return -1 if l==c else l
        # count=0
        # col=0
        # for i in range(r-1,-1,-1):
        #     cur=0
        #     idx=binSearch(i,col,c-1)
        #     if idx==-1: return count
        #     cur+=c-idx
        #     col=idx
        #     count+=cur
        # return count
        
        # O(n+m) solution
        count=0
        i=len(grid)-1
        j=0
        while j<len(grid[i]) and i>=0:
            if grid[i][j]<0:
                count+=(len(grid[i])-j)
                i-=1
            else:
                j+=1
        return count