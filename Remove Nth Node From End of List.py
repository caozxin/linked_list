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

        if not head: # base case
            
            return head
        
        print(" ", head.val, n)
        self.remove_nth_from_end(head.next, n)
        

        while n > 0:
            n -= 1
            print(head.val, n)
        print("n", n)
        if n == 0:
            print(head.val, "next step")
            #remove current node:
            return
        
        return head
