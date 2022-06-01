class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=-float('inf')
        localMax=-float('inf')
        for i in range(len(nums)):
            localMax=max(localMax+nums[i],nums[i])
            if localMax>maxSum:
                maxSum=localMax
        return maxSum