class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap=set()
        for windowEnd in range(len(nums)):
            if len(hashMap)>=k+1:
                hashMap.remove(nums[windowEnd-k-1])
            if nums[windowEnd] in hashMap:
                return True
            hashMap.add(nums[windowEnd])
        return False