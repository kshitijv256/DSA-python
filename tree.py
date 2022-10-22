# Created by Kshitij on 18/2/2022

from queueFile import Queue

class Node:
    def __init__(self, value):
        self.data = value
        self.lchild = None
        self.rchild = None
        
def insert(root,value):
        if root is None:
            root = Node(value)
        elif value <= root.data:
            if root.lchild is None:
                root.lchild = Node(value)
            else:
                insert(root.lchild,value)    
        else:
            if root.rchild is None:
                root.rchild = Node(value)
            else:
                insert(root.rchild,value)

def inTraversal(root):
    if root is None:
        return "\nTree is Empty"
    else:
        inTraversal(root.lchild)
        print(root.data)
        inTraversal(root.rchild)

def postTraversal(root):
    if root is None:
        return "\nThe Tree is Empty"
    else:
        postTraversal(root.lchild)
        postTraversal(root.rchild)
        print(root.data)

def preTraversal(root):
    if root is None:
        return "\nThe Tree is Empty"
    else:
        print(root.data)
        preTraversal(root.lchild)
        preTraversal(root.rchild)

def BFTraversal(root):
    tempQ = Queue()
    if root is None:
        return "\nThe Tree is Empty"
    else:
        tempQ.enqueue(root)
        while not(tempQ.isEmpty()):
            temp = tempQ.dequeue()
            if temp.data.lchild is not None:
                tempQ.enqueue(temp.data.lchild)
            if temp.data.rchild is not None:
                tempQ.enqueue(temp.data.rchild)
            print(temp.data.data)

def search_rec(root,query):
    if root is not None:
        if query == root.data:
            return "Found it"
        elif query < root.data:
            return search_rec(root.lchild,query)
        elif query > root.data:
            return search_rec(root.rchild,query)
        else:
            return "Not Found"
    return "Not Found"

def search_iter(root,query):
    temp = root
    while temp is not None:
        if temp.data == query:
            return 'Found it MF!'
        elif temp.data > query:
            temp = temp.lchild
        else:
            temp = temp.rchild
    else:
        return "Not found"
        


def min(root):
    temp = root
    while(temp.lchild is not None):
        temp = temp.lchild
    return temp

def delete(root,value):
    if root is None:
        return root
    if value < root.data:
        root.lchild = delete(root.lchild,value) #1
    elif value > root.data:
        root.rchild = delete(root.rchild,value) #2
    else:
        if root.lchild is None:
            temp = root.rchild
            root = None
            return temp
        elif root.rchild is None:
            temp = root.lchild
            root = None
            return root
        
        temp = min(root.rchild,value)
        root.data = temp.data
        root.rchild = delete(root.rchild,value) #3
    
    # Executed after all recursive functions [#1 #2 #3] return there values
    # Main root of the tree may change if value provided for delete was root itself
    return root 


newTree = Node(16)
insert(newTree, 12)
insert(newTree, 10)
insert(newTree, 18)
insert(newTree, 11)
insert(newTree, 9)
insert(newTree, 20)
insert(newTree, 14)
insert(newTree, 17)

delete(newTree,14)
q = int(input("Enter query"))
print(search_iter(newTree,q))

#BFTraversal(newTree)

#print(newTree.lchild.lchild.rchild.data)