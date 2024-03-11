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
        # Define a dummy node to handle edge cases --> need to further review dummy node method for linked list
        dummy = ListNode(0)
        dummy.next = head
        prev_head = dummy
        curr_head = dummy
        
        # Move the prev_head pointer ahead by n+1 steps
        for i in range(n + 1):
            prev_head = prev_head.next # this makes prev_head become the previous node of the node to be deleted_node
        # print(first.val)
        # exit()
        # Move both pointers together until the first pointer reaches the end
        while prev_head is not None:
            prev_head = prev_head.next
            curr_head = curr_head.next
        
        # Remove the nth node from the end
        curr_head.next = curr_head.next.next
        
        return dummy.next
