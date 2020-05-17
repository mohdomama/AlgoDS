'''
    link: https://practice.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1
    Function to add two numbers represented 
    in the form of the linked list.
    
    Function Arguments: head_a and head_b (heads of both the linked lists)
    Return Type: head of the resultant linked list.
    
    __>IMP : numbers are represented in reverse in the linked list.
    Ex:
        145 is represented as  5->4->1.
    
    resultant head is expected in the same format.
    
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''


def addBoth(head_a, head_b):
    # There should be a better way to write this
    head_c = None
    itr_c = None
    carry = 0
    sum_itr = 0
    while head_a != None or head_b != None:
        if itr_c == None:
            itr_c = Node(0)
            head_c = itr_c

        else:
            itr_c.next = Node(0)
            itr_c = itr_c.next

        if head_a == None:
            sum_itr = head_b.data + carry
            carry = int(sum_itr / 10)
            sum_itr = sum_itr % 10

            itr_c.data = sum_itr

            head_b = head_b.next

        elif head_b == None:
            sum_itr = head_a.data + carry
            carry = int(sum_itr / 10)
            sum_itr = sum_itr % 10

            itr_c.data = sum_itr

            head_a = head_a.next

        else:
            sum_itr = head_a.data + head_b.data + carry
            carry = int(sum_itr / 10)
            sum_itr = sum_itr % 10

            itr_c.data = sum_itr

            head_a = head_a.next
            head_b = head_b.next

    if carry != 0:
        itr_c.next = Node(carry)
        itr_c = itr_c.next

    return head_c
