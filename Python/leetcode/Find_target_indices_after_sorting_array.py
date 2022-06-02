class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans=[]
        if target not in nums:
            return ans
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                ans.append(mid)
                left=mid-1
                right=mid+1
                while left>=0 and nums[left]==target:
                    ans.append(left)
                    left-=1
                while right <len(nums) and nums[right]==target:
                    ans.append(right)
                    right+=1
                return sorted(ans)
            elif nums[mid]>target:
                r=mid
            else:
                l=mid+1