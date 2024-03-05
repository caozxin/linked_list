from lintcode import (
    ListNode,
)

"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # write your code here

        #we start with insert operation:
        if not l1 or not l2:#base case to exit
            return
        print(l1.val, l2.val)

        self.merge_two_lists(l1, l2.next) # recurse everything after current ListNode

        if l1.val >= l2.val: # operations on the current ListNode
            print("operation starts: ", l1.val, l2.val)
            temp = l2.next #(temp = l2.next = '2')
            l1.next = temp #(l1.next = '2')
            l2.next = l1 #(l2.next = '0'.next = l1)

        return l2
        

