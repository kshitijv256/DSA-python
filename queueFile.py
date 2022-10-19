

class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, value):
        newNode = Node(value)
        if self.front is None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = self.rear.next
            self.rear.next = None
    def isEmpty(self):
        if self.front is None:
            return True
        else:
            return False
    def dequeue(self):
        if self.isEmpty():
            return "The Queue is Empty"
        else:
            temp = self.front
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
            return temp
    def traverse(self):
        temp = self.front
        while temp is not None:
            print(temp.data)
            temp = temp.next
    def delete(self):
        self.front = None
        self.rear = None






#que = Queue()
#que.enqueue(2)
#que.enqueue(4)
#que.enqueue(8)
#que.enqueue(16)
#que.dequeue()
#que.enqueue(32)
#que.dequeue()
#que.traverse()



        