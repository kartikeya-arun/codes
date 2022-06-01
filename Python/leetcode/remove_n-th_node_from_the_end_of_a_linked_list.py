# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        
		# let fast ptr travel n nodes first
        while fast and n > 0:
            fast = fast.next
            n -= 1
        
		# if fast is None, then we remove the first node
        if not fast:
            return head.next
        
		# let both fast and slow ptrs travel together
		# since fast ptr travelled n nodes alr
		# it means now the slow ptr will travel (L-n) nodes, thus nth node from end
        while fast:
            prev = slow
            fast = fast.next
            slow = slow.next
            
        prev.next = slow.next
        
        return head