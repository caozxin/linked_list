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
    def merge_two_lists_default(self, l1: ListNode, l2: ListNode) -> ListNode: # this is recursive
        # write your code here

        #we start with insert operation:
        if not l1 or not l2:#base case to exit
            return l2 or l1 # we return the remaining not None list
        print(l1.val, l2.val)

        if l1.val <= l2.val:
            l1.next = self.merge_two_lists(l1.next, l2)  # recurse everything after l1 current ListNode
            return l1
        else:
            l2.next = self.merge_two_lists(l1, l2.next) # recurse everything after l2 current ListNode
            return l2

    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        cur = dummyHead
        while(1):
            if l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next       
                cur = cur.next
            else:
                cur.next = l1 if l1 else l2
                break
        return dummyHead.next


### update 05/27/26 my version:
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 or not list2:
            return list1 or list2

        nums = []

        while list1:
            nums.append(list1.val)
            list1 = list1.next

        while list2:
            nums.append(list2.val)
            list2 = list2.next

        nums.sort()

        dummy = ListNode() # Set up dummy, Then NEVER move dummy. Only move curr.
        curr = dummy

        for val in nums:
            curr.next = ListNode(val)
            curr = curr.next

        # print(dummy)
        return dummy.next

### update 05/27/2026 better version:
class Solution:
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()
        curr = dummy

        while list1 and list2:

            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        curr.next = list1 or list2

        return dummy.next
