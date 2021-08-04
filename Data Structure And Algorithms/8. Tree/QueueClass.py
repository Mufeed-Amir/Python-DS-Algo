class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        tempNode=self.head
        while tempNode:
            yield tempNode
            tempNode=tempNode.next
    def __str__(self):
        dlist=[str(x.val) for x in self]
        return " <-- ".join(dlist)
    
    def enQueue(self,data):
        newNode=ListNode(data)
        if self.head==None:
            self.tail=newNode
            self.head=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
    def deQueue(self):
        if not self.isMT():
            value=self.head.val
            self.head=self.head.next
            return value
    def isMT(self):
        if self.head==None:
            return True
        else:
            return False
