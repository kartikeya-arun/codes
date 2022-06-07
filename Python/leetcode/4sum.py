class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans,qd=[],[]
        
        # NAIVE
        
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)-2):
        #         p1=j+1
        #         p2=len(nums)-1
        #         while p1<p2:
        #             curSum=nums[i]+nums[j]+nums[p1]+nums[p2]
        #             if curSum==target and [nums[i],nums[j],nums[p1],nums[p2]] not in ans:
        #                 ans.append([nums[i],nums[j],nums[p1],nums[p2]])
        #             elif curSum>target:
        #                 p2-=1
        #             else:
        #                 p1+=1
        # return ans

        # Generic K sum algorithm

        def kSum(k,start,target):
            if k!=2:
                for i in range(start,len(nums)-k+1):
                    if i>start and nums[i]==nums[i-1]:
                        continue
                    qd.append(nums[i])
                    kSum(k-1,i+1,target-nums[i])
                    qd.pop()
                return
            # base case
            l,r=start,len(nums)-1
            while l<r:
                if nums[l]+nums[r]<target:
                    l+=1
                elif nums[l]+nums[r]>target:
                    r-=1
                else:
                    ans.append(qd+[nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        kSum(4,0,target)
        return ans