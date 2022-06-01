class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M,N=len(grid),len(grid[0])
        ans=[[0]*N for i in range(M)]
        for r in range(M):
            for c in range(N):
                newVal=(r*N+c+k)%(M*N) # find the index of grid[r][c] in 1-D array for shifting and then shift k places
                newR,newC=newVal//N,newVal%N # find the index of the element after shifting in 2-D matrix
                ans[newR][newC]=grid[r][c]
        return ans