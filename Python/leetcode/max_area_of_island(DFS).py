class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # BFS approach
#         seen=set() # maintaining a set for visited cells
#         def area(r,c):
#             if not (0<=r<len(grid) and 0<=c<len(grid[0]) and (r,c) not in seen and grid[r][c]):
#                 return 0 # setting a base case
#             seen.add((r,c)) # adding visited cells to set
#             return (1+area(r-1,c)+area(r+1,c)+area(r,c-1)+area(r,c+1)) # recursively visiting every cell to find the size of area for all islands
#         return max(area(r,c) for r in range(len(grid)) for c in range(len(grid[0]))) # returning the max area
    
        # DFS appreach
        seen=set()
        ans=0
        for r0,row in enumerate(grid):
            for c0,val in enumerate(row):
                if val and (r0,c0):
                    shape=0
                    stack=[(r0,c0)]
                    seen.add((r0,c0))
                    while stack:
                        r,c=stack.pop()
                        shape+=1
                        for rn,cn in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                            if (0<=rn<len(grid) and 0<=cn<len(grid[0]) and grid[rn][cn] and (rn,cn) not in seen):
                                stack.append((rn,cn))
                                seen.add((rn,cn))
                    ans=max(ans,shape)
        return ans