# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
#         Inintiate a dummy node so that edge cases can be easily handled (If we need to reverse from the head or the head changes after reversal. dummy node always points to the head)
        dummy=ListNode(0,head)
#     Initiate tow pointers prevLeft and cur which point to current node and node before it (initially point to dummy and lead). Here prevLeft stores te node before the left index to set the pointers at the end
        cur=head
        prevLeft=dummy
#         Initiate a prev pointer similar to standard reversing algorithm
        prev=None
#     Phase1: Loop for left number of nodes to reach the position from which reversing needs to be started while updating prevLeft
        for i in range(left-1):
            prevLeft=cur
            cur=cur.next
#     Phase2: Start reversing the links in the given range        
        for i in range(right-left+1):
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
#     Phase3: Set the pointers so that links are established with rest of the list        
        prevLeft.next.next=cur
        prevLeft.next=prev
#         Return head
        return dummy.next