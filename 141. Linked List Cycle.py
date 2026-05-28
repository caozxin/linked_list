# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = list()

        dummy = head
        curr = dummy

        while curr:
            if curr not in seen:
                seen.append(curr)
                curr = curr.next
            else:
                return True

        return False
