class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class MyLinkedList:

    def __init__(self):
        self.head=None
        self.length=0
    def get(self, index: int) -> int:
        if index<0 or index>self.length-1:
            return -1
        else:
            node=self.head
            if node:
                for i in range(index):
                    node=node.next
                return node.val
            else:
                return -1
    def addAtHead(self, val: int) -> None:
        cur=Node(val,self.head)
        self.head=cur
        self.length+=1
    def addAtTail(self, val: int) -> None:
        cur=Node(val)
        node=self.head
        if node:
            for i in range(self.length-1):
                node=node.next
            node.next=cur
        else:
            self.head=cur
        self.length+=1
    def addAtIndex(self, index: int, val: int) -> None:
        cur=Node(val)
        if index<0 or index>self.length:
            return
        elif index==0:
            self.addAtHead(val)
        else:
            node=self.head
            if node:
                for i in range(index-1):
                    node=node.next
                cur.next=node.next
                node.next=cur
            else:
                return
        self.length+=1
    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>self.length-1:
            return
        elif index==0:
            self.head=self.head.next
        else:
            node=self.head
            if node:
                for i in range(index-1):
                    node=node.next
                node.next=node.next.next
            else:
                return
        self.length-=1
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)