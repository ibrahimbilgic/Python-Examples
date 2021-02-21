class Node:
    def __init__(self,value,left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return "Node(" + str(self.value) +")"
    
def bfs(node,queue):
    queue.append(node)
    while len(queue) > 0:
        node = queue.pop(0)
        if node is not None:
            print(node)
            queue.append(node.left)
            queue.append(node.right)
            
mytree = Node('A',Node('B',Node('D'),Node ('E')),Node('C',Node('F'),Node('G')))
bfs(mytree,[])
        