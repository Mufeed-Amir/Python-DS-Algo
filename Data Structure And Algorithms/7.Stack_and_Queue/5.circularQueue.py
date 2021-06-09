class CircularQueue:

    def __init__(self,sizeMax):
        self.list=sizeMax*[None]
        self.sizeMax=sizeMax
        self.start=-1
        self.top=-1

    def __str__(self):
        items=[str(x) for x in self.list]
        return " <-- ".join(items)
     
    def isFull(self):
        if self.top + 1==self.start:
            return True
        elif self.start==0 and self.top+1==self.sizeMax:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top==-1:
            return True
        else: 
            return False

    def enqueue(self,value):
        if self.isFull():
            return "Queue is Full"

        else: 
            if self.top==self.sizeMax:
                self.top=0
            else:
                self.top +=1
                if self.start==-1:
                    self.start=0
            self.list[self.top]=value

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            start=self.start
            firstElement=self.list[start]
            if self.start==self.top:
                self.start=-1
                self.top=-1
            elif self.start + 1 == self.sizeMax:
                self.start=0
            else:
                self.start=self.start + 1     
            self.list[start]=None  
            return firstElement 
        
    def delete(self):
        self.start=-1
        self.top=-1
        self.list=self.sizeMax * [None]

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:    
            return self.list[self.start]          

cqueue=CircularQueue(3)
cqueue.enqueue(1)
cqueue.enqueue(2)
cqueue.enqueue(3)
print(cqueue)
print(cqueue.dequeue())
print(cqueue)
print(cqueue.isEmpty())
print(cqueue.isFull())
print(cqueue.peek()) 
cqueue.delete()
print(cqueue)  