#User function Template for python3



class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


def in_order(node, level, traversal):
    if node == None:
        return
    
    # val = traversal.get(level, [])
    # traversal[level] = val.append(node)
    if level in traversal:
        traversal[level].append(node)
    else:
        traversal[level] = [node]
    
    in_order(node.left, level-1, traversal)
    in_order(node.right, level+1, traversal)
    
    
def verticalOrder(root):
    traversal = {}
    in_order(root, 0, traversal)
    for key in sorted(traversal.keys()):
        for elem in traversal[key]:
            print(elem.data, end=' ')

def main():
    root  = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(-1)
    root.right.right = Node(3)
    root.right.right.right = Node(4)
    root.right.right.right.right = Node(5)

    verticalOrder(root)

if __name__ == '__main__':
    main()