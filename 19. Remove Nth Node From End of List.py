class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def remove_nth_from_end_version2(self, head, n):
        dummy = ListNode(0)
        cur = dummy
        prev = dummy
        node = head
        cur.next = head
        count = 0

        while cur.next is not None: # this is counting the lenght of the list. 
            cur = cur.next
            count += 1

        for i in range(count-n):
            node = node.next
            prev = prev.next

        deleted_node = node
      
        prev.next = deleted_node.next

        return dummy.next

    def remove_nth_from_end_default(self, head: ListNode, n: int) -> ListNode:
        # Define a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        # Move the first pointer ahead by n+1 steps
        for i in range(n + 1):
            first = first.next
        
        # Move both pointers together until the first pointer reaches the end
        while first is not None:
            first = first.next
            second = second.next
        
        # Remove the nth node from the end
        second.next = second.next.next
        
        return dummy.next

    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        # Define a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev_head = dummy
        curr_head = dummy
        
        # Move the prev_head pointer ahead by n+1 steps
        for i in range(n + 1):
            prev_head = prev_head.next # this makes prev_head become the previous node of the node to be deleted_node
        # print(first.val)
        # exit()
        # Move both pointers together until the first pointer reaches the end. --> this step we move curr_head to the node to be deleted_node
        while prev_head is not None:
            prev_head = prev_head.next
            curr_head = curr_head.next
        # print("prev_head.val, curr_head.val")
        # print(prev_head.val, curr_head.val)
        # print(curr_head.val, curr_head.next.val)
        # Remove the nth node from the end
        curr_head.next = curr_head.next.next
        # print(curr_head.val, curr_head.next.val)
        
        return dummy.next # we should return the updated head from dummy.next



### update 05/28/26:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        fast, slow = dummy, dummy

        for _ in range(n):
            fast = fast.next
        
        # print(fast)

        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        # print(slow) # this is the node needs to be removed

        slow.next = slow.next.next # only .next make actual changes, slow or fast are just pointers.

        # print(dummy)
        return dummy.next
