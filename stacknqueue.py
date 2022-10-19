class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

#stack and queue

class stack:
    def __init__(self):
        self.head = None
        self.top = None
        
    #stack ops
    def push(self,data):
        newNode = Node(data)
        if self.head:
            curr = self.head
            while curr:
                curr = curr.next
            curr = newNode
        else:
            self.head = newNode
    def pop(self):
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            temp = curr
            curr = None
            return temp.data
        else:
            return self.head
    
    
class queue:
    def __init__(self):
        self.head = None
        self.top = None
    #queue ops
    def enqueue(self,data):
        newNode = Node(data)
        if self.head:
            self.top = self.top.next
            self.top = newNode
        else:
            self.head = newNode
            self.top = self.head
    def dequeue(self):
        if self.head:
            temp = self.head
            self.head = self.head.next
            return temp.data
        else:
            return self.head



s = "Kshitij"
obj1 = stack()
obj2 = queue()
for i in s:
    obj1.push(i)
    obj2.enqueue(i)

curr = obj1.head
while curr:
    print(curr.data)
    curr = curr.next