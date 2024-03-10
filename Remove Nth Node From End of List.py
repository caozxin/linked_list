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
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        # write your code here
        abs_pos = -n
        # we need to keep track of the previous node to conduct the deletion: 

        def traversal(pre_head, head, n, abs_pos):
            if not head: # base case
                return head
            n -= 1
            # abs_pos -= 1
            if pre_head: 
                print(" ", pre_head.val, head.val, n, abs_pos)
            # self.remove_nth_from_end(head.next, n)
            traversal(head, head.next, n, abs_pos)

            if n == abs_pos:
                print("found it!: ", pre_head.val, head.val)
                #start deleltion of the current node: --> we should change the current head
                temp = head.next # (head.next = 5)
                head = pre_head
                head.next = temp
        
            return head
        traversal(None, head, n, abs_pos)
        return head
