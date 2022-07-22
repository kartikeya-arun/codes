# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
#         create two dummy nodes for two parts of the answer before and after
        before=before_head=ListNode(0,None)
        after=after_head=ListNode(0,None)
#         Iterate over the given list while adding the node<x to before list and adding node>=x to after list
        while head:
            if head.val<x:
                before.next=head
                before=before.next
            else:
                after.next=head
                after=after.next
            head=head.next
#             Set after.next to point at null since this is the end of list
        after.next=None
#     Set before.next to after_head.next to join the two parts
        before.next=after_head.next
#     Return before_head.next as answer
        return before_head.next