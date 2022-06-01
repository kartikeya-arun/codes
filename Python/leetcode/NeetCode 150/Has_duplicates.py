class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Too naive
#         counts=Counter(nums)
#         for i in counts.keys():
#             if counts[i]>1:
#                 return True
#         return False
        
        # Hashset
        # seen=set()
        # for i in nums:
        #     if i in seen:
        #         return True
        #     else:
        #         seen.add(i)
        # return False
        
        # Sorting
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False