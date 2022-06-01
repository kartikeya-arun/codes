class Solution:
    def partitionLabels(self, s: str) -> List[int]:
#         if not s or len(s)==0:                                   --was faster than below solution
#             return None
#         ans=[]
#         n=len(s)
#         letter_indices=dict(zip(string.ascii_lowercase,[0]*26))
#         for i in range(n):
#             letter_indices[s[i]]=i
            
#         start=0
#         end=0
#         for i in range(n):
#             end=max(end,letter_indices[s[i]])
#             if i==end:
#                 ans.append(end-start+1)
#                 start=end+1
#         return ans
        last={c: i for i,c in enumerate(s)}
        j=anchor=0
        ans=[]
        for i,c in enumerate(s):
            j=max(j,last[c])
            if j==i:
                ans.append(i-anchor+1)
                anchor=i+1
        return ans