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
    def reverse(self, head: ListNode) -> ListNode:
        # write your code here

        reversed_head = None 
        while head != None:
            #set vars:
            temp = head.next # this is a node
            head.next = reversed_head
            reversed_head = head
            head = temp
            
        return reversed_head
