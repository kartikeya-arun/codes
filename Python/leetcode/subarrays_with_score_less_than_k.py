class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        sm=0
        j=0
        ans=0
        for i in range(len(nums)):
            while j<len(nums) and (sm+nums[j])*(j-i+1)<k:
                sm+=nums[j]
                j+=1
            ans+=j-i
            sm-=nums[i]
        return ans