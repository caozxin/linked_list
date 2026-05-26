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


### update 05/26/26:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        stack = list()
        while head:
            print(head.val)
            stack.append(head.val)
            head = head.next

        print(head, stack)
        head = ListNode(stack.pop()) # we need to initial new head
        curr = head
        while stack:
            curr.next = ListNode(stack.pop())
            curr = curr.next
        print(head)

        return head


### 05/26/26 better version:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next # placeholder
            curr.next = prev # main swap
            prev = curr # clean up afterwards
            curr = nxt # moving to next

        return prev
