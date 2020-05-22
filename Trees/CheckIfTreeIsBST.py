'''
Problem: https://practice.geeksforgeeks.org/problems/check-for-bst/1
In order traversal of BST gives increasing order.
- Note: we have to check the condition that equal elements always go towards
the left. Hence we use the explored stack.
'''


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def in_order(node, stack, explored):
    if node == None:
        return True

    B1 = in_order(node.left, stack, explored)

    B2 = True
    if len(stack) > 0:
        if node.data < stack[-1]:
            B2 = False
        elif node.data == stack[-1] and not explored[-1]:
            B2 = False

    stack.append(node.data)
    explored.append(False)

    sno = len(stack) - 1

    B3 = in_order(node.right, stack, explored)

    explored[sno] = True

    return B1 and B2 and B3


def isBST(node):

    stack, explored = [], []
    return in_order(node, stack, explored)
