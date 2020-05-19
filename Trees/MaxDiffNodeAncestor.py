'''
Problem: https://practice.geeksforgeeks.org/problems/maximum-difference-between-node-and-its-ancestor/1
- We use two stacks. Max so far and Min so far.
'''


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def pre_order(node, mins, maxs, root, maxd):
    if node == None:
        return maxd
    if node != root:
        if mins[-1] - node.data > maxd:
            maxd = mins[-1] - node.data
        if maxs[-1] - node.data > maxd:
            maxd = maxs[-1] - node.data

        if node.data >= maxs[-1]:
            maxs.append(node.data)
        if node.data <= mins[-1]:
            mins.append(node.data)

    maxd = pre_order(node.left, mins, maxs, root, maxd)
    maxd = pre_order(node.right, mins, maxs, root, maxd)

    if maxs[-1] == node.data:
        maxs.pop()
    if mins[-1] == node.data:
        mins.pop()

    return maxd


def maxDiff(root):
    '''
    :param root: Root of given tree
    :return: Integer
    '''
    maxd = -999999
    mins, maxs = [root.data], [root.data]
    maxd = pre_order(root, mins, maxs, root, maxd)
    print(maxd)


def main():
    root = Node(5)
    root.left = Node(2)
    root.right = Node(1)
    maxDiff(root)


if __name__ == '__main__':
    main()
