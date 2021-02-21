#DEPTH FIRST SEARCH WITH PYTHON
#first method
class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right =right
    def __str__(self):
        return "Node(" + str(self.value) + ")"
            
        
def walk(tree):#recursive method # using the call stack..
    if tree is not None:
        print(tree) # if we use print here, it is preorder traversel
        walk(tree.left)
        # print(tree) if we use print here, it is inorder traversel 
        walk(tree.right)
        # print(tree) if we use print here, it is postorder traversel

#second method
#using our own explicit stack
def walk2(tree,stack):
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            print(node)
            stack.append(node.right)
            stack.append(node.left)


mytree = Node('A',Node('B',Node('D'),Node ('E')),Node('C',Node('F'),Node('G')))
walk(mytree) #walk called..
walk2(mytree,[]) # walk2 called..