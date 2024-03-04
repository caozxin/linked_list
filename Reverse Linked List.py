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
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head: ListNode) -> ListNode: # recursive approach
        if not head or not head.next:# base case
            return head

        reversed = self.reverse(head.next) # recurse everything after current ListNode

        head.next.next = head; # operations on the current ListNode, so that current linking will be nullafiled and backward linking will be added
        head.next = None

        return reversed


    def reverse_default(self, head: ListNode) -> ListNode:
        # write your code here
        curr_list = []
        # curr_val = None
        def linked_list_traversal(head:ListNode): 
            if not head:
                return curr_list
            curr_val = head.val
            print(curr_val)
            curr_list.append(curr_val)
            head.val = None
            # curr_val = val
            next = self.reverse(head.next)
            head.val = curr_val
        

        result_list = linked_list_traversal(head)
        print("curr_list", curr_list)

        return head
