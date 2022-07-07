class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # m=len(grid)
        # n=len(grid[0])
        # for i in range(m):
        #     grid[i]+=[float('inf')]
        # grid+=[[float('inf')]*(n+1)]
        # grid[-1][-2]=0
        # for r in range(m-1,-1,-1):
        #     for c in range(n-1,-1,-1):
        #         grid[r][c]+=min(grid[r+1][c],grid[r][c+1])
        # return grid[0][0]
    
        m=len(grid)
        n=len(grid[0])
        row=[float('inf')]*(n+1)
        row[-2]=0
        for r in range(m-1,-1,-1):
            newRow=grid[r]+[float('inf')]
            for c in range(n-1,-1,-1):
                newRow[c]+=min(newRow[c+1],row[c])
            row=newRow
        return row[0]