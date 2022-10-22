class node():
    def __init__(self,data = None):
        self.data = data
        self.next = None
class linklist():
    def __init__(self,node):
        self.head = node
    def append(self,value):
        curr = self.head
        if curr:
            while curr.next:
                curr = curr.next
            curr.next = node(value)
        else:
            self.head = node(value)
    def pop(self):
        curr = self.head
        if curr:
            if curr.next:
                while curr.next.next:
                    curr = curr.next
                temp = curr.next
                curr.next = None
                return temp
            else:
                self.head = None
                return curr
        else:
            return None
    def show(self):
        curr = self.head
        if curr:
            while curr:
                print(curr.data)
                curr = curr.next
        else:
            print('Empty list')


### Driver Code
'''
list = linklist(node(5))
list.append(6)
list.append(7)
list.append(8)
print()
list.show()
print()
print(list.pop().data)
print(list.pop().data)
print()
list.show()
'''