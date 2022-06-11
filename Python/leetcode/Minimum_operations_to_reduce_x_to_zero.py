class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # Maximum subarray
        
#         dp=[0]
#         cur=0
#         ans=-1
#         for i in range(len(nums)):
#             cur+=nums[i]
#             dp.append(cur)
#         lookup={v:i for i,v in enumerate(dp)}
        
#         y=sum(nums)-x
#         for val,idx in lookup.items():
#             if val+y in lookup:
#                 ans=max(ans,lookup[val+y]-idx)
#         return ans if ans==-1 else len(nums)-ans
    
        #Sliding window
    
        target = sum(nums) - x
        curr_sum, max_len = 0, 0
        start_idx = 0
        found = False
        for end_idx in range(len(nums)):
            curr_sum += nums[end_idx]
            while start_idx <= end_idx and curr_sum > target:
                curr_sum -= nums[start_idx]
                start_idx += 1
            if curr_sum == target:
                found = True
                max_len = max(max_len, end_idx - start_idx + 1)

        return len(nums) - max_len if found else -1