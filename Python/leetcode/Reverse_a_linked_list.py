# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative
        cur=head
        prev=None
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        return prev
        
        # Recursive
#         if not head:
#             return
        
#         newHead=head
#         if head.next:
#             newHead=self.reverseList(head.next)
#             head.next.next=head
#         head.next=None
#         return newHead