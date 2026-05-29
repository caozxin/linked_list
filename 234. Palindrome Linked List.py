# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # if not head or head.next:
        #     return 

        dummy = ListNode(0, head) # this is to creat a new node based on head node
        # dummy = head # this is a pointer to the existing head node
        slow = dummy
        fast = dummy

        # 1. Use fast/slow pointers to find the midpoint
        while fast.next and fast.next.next: # this while loop end until the fast.next.next becomes None
            slow = slow.next
            fast = fast.next.next
        # print(slow)
        # 2. Save the head of the second part
        second_head = slow.next
        # print(second_head)
        # 3. Cut the list by setting next to None
        slow.next = None

        # Returns heads of both lists
        # print(head, second_head)
        #reverse the second_head:
        prev = None
        curr = second_head

        while curr: # this while loop end until the last node of curr becomes None
            nxt = curr.next # store the next node
            curr.next = prev
            prev = curr
            curr = nxt
            # print(prev, curr, nxt)

        while prev and head: # this while loop end if either prev or head node becomes None
            if prev.val != head.val:
                # print('head', head)
                # print('prev', prev)
                return False
            else:
                prev = prev.next
                head = head.next
        return True
