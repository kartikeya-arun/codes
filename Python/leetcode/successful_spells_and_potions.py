class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans=[]
        for s in spells:
            idx=bisect_left(potions,math.ceil(success/s))
            ans.append(len(potions)-idx)
        return ans