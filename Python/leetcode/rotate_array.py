def reverse(nums,low,high):
    while low<high:
        nums[low],nums[high]=nums[high],nums[low]
        low+=1
        high-=1
nums=list(map(int,input().split()))
k=int(input())
n=len(nums)
# if n==2:
#     if k%2!=0:
#         l=nums[0]
#         nums[0]=nums[n-1]
#         nums[n-1]=l
# else:
#     l=len(nums)
#     for i in nums[:n-k]:
#         nums.append(i)
#     del nums[:len(nums)-l]
# print(nums)

# if k>n:
#     k=k%n
#     nums=nums[n-k:]+nums[:n-k]
# else:
#     nums=nums[n-k:]+nums[:n-k]

reverse(nums,0,n-k-1)
reverse(nums,n-k,n-1)
reverse(nums,0,n-k)

print(nums)