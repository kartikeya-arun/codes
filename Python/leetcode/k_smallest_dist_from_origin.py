class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k==len(points): return points
        h=[]
        for x,y in points:
            dist=x**2+y**2
            h.append([dist,x,y])
        heapify(h)
        ans=[]
        while k:
            ans.append(heappop(h)[1:])
            k-=1
        return ans