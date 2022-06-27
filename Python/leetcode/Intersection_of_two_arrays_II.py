class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        # Hashmap
        # c=Counter(nums1)
        # for i in nums2:
        #     if c[i]>0:
        #         ans.append(i)
        #         c[i]-=1
        # return ans
    
        # Two pointer
        i,j=0,0
        nums1.sort()
        nums2.sort()
        while i<len(nums1) and j<len(nums2):
            if nums1[i]>nums2[j]:
                j+=1
            elif nums2[j]>nums1[i]:
                i+=1
            else:
                ans.append(nums1[i])
                i+=1
                j+=1
        return ans