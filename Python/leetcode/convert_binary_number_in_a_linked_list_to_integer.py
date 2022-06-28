# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # ans=''
        # cur=head
        # while cur:
        #     ans+=str(cur.val)
        #     cur=cur.next
        # return int(ans,2)
    
        # num=head.val
        # while head.next:
        #     num=num*2+head.next.val
        #     head=head.next
        # return num
        
        num=head.val
        while head.next:
            num=num<<1|head.next.val
            head=head.next
        return num