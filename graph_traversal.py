
# class Node:
#     def __init__(self,data):
#         self.value = data
#         self.left = None
#         self.right = None


# adjMat = []
# for i in range(n):
#     adjMat.append([])



# DFS
def dfs(adjMat,root):
    print("DFS Traversal of the given graph is:")
    stack = []
    visited = []
    mat = adjMat.copy()
    r = root
    stack.append(r)
    visited.append(r)
    while stack:
        i = stack.pop()
        print(i,end='\t')
        for j in mat[i-1]:
            if j in visited: continue
            else:
                stack.append(j)
                visited.append(j)
                

    print()


# BFS
def bfs(adjMat,root):
    print("BFS Traversal of the given graph is:")
    mat = adjMat.copy()
    r = root
    myQueue = []
    visited = []
    myQueue.append(r)
    visited.append(r)

    while myQueue:
        i = myQueue.pop(0)
        print(i,end='\t')
        for j in mat[i-1]:
            if j in visited: continue
            else:
                myQueue.append(j)
                visited.append(j)
                
    print()

adjMat = []
nodes = int(input())
for i in range(nodes):
    x = list(map(int, input().split()))
    adjMat.append(x)

print(adjMat)
dfs(adjMat,2)
bfs(adjMat,2)



        

