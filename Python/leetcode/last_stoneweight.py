class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones.sort()
        # while len(stones)>1:
        #     if stones[len(stones)-1]==stones[len(stones)-2]:
        #         stones.pop()
        #         stones.pop()
        #         stones.sort()
        #     else:
        #         stones[len(stones)-1]=stones[len(stones)-1]-stones[len(stones)-2]
        #         stones.remove(stones[len(stones)-2])
        #         stones.sort()
        # return max(stones) if stones!=[] else 0
        stones=[-s for s in stones]     # setting all elements to negative to use min heap as max heap
        heapq.heapify(stones)
        while len(stones)>1:
            first=heapq.heappop(stones)
            second=heapq.heappop(stones)
            if second>first:    # beacause all elements are negative
                heapq.heappush(stones,first-second)
        return abs(stones[0]) if stones else 0      # Since all values are negative so abs() value has to be returned