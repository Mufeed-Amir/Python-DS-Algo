class ListNode:
    def __init__(self,val=None):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __iter__(self):
        tempNode=self.head
        while tempNode:
            yield tempNode
            tempNode=tempNode.next
            
class Queue:
    def __init__(self):
        self.linkedlist=LinkedList()
    
    def __str__(self):
        if self.linkedlist.head==None:
            return "Queue is empty"
        else:    
            values=[str(x.val) for x in self.linkedlist]
            return "<--".join(values)
    

    def enQueue(self,value):
        if self.linkedlist.head==None:
            self.linkedlist.head=ListNode(value)
            self.linkedlist.tail=self.linkedlist.head
        else:
            self.linkedlist.tail.next=ListNode(value)
            self.linkedlist.tail=self.linkedlist.tail.next
    def isEmpty(self):
        if self.linkedlist.head==None:
            return True 
        else:
            return False
    def deQueue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            k=self.linkedlist.head.val
            if self.linkedlist.head==self.linkedlist.tail:
                k=self.linkedlist.head.val
                self.linkedlist.head=None
                self.linkedlist.tail=None
                return k
            else:
                self.linkedlist.head=self.linkedlist.head.next
                return k
            
    def delete(self):
        self.linkedlist.head=None
        self.linkedlist.tail=None
        print("Queue is successfully deleted!")
    
if __name__=="__main__":
    queue=Queue()
    queue.enQueue(34)
    queue.enQueue(28)
    queue.enQueue(21)
    queue.enQueue(13)
    print(queue)
    print(queue.deQueue())
    print(queue)
    queue.delete()
    print(queue)