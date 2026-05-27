# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = list()
        dummy = head
        curr = dummy

        while curr:
            stack.append(curr.val)
            curr = curr.next
        # print(stack)

        mid = (len(stack) // 2 ) 

        # print('mid', mid, stack[mid:])

        dummy = ListNode(None)
        new_curr = dummy
        new_stack = stack[mid:]

        for each in new_stack:
            new_curr.next = ListNode(each)
            new_curr = new_curr.next
            # 
        # print(dummy)

        return dummy.next
