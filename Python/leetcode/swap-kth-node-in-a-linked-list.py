# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # cur=head
        # size=0
        # while cur:
        #     size+=1
        #     cur=cur.next                                  # Faster
        # l=k
        # r=size-k
        # nodeL=head
        # nodeR=head
        # while l-1>0:
        #     nodeL=nodeL.next
        #     l-=1
        # while r>0:
        #     nodeR=nodeR.next
        #     r-=1
        # nodeL.val,nodeR.val=nodeR.val,nodeL.val
        # return head
        
        slow=head
        fast=head
        
        for i in range(k-1):
            slow=slow.next
        
        start=slow
        while slow.next:
            slow=slow.next
            fast=fast.next
        start.val,fast.val=fast.val,start.val
        return head