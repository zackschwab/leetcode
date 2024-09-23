# 19. Remove nth node from Linked List
[Link](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=study-plan-v2&envId=top-interview-150)


For this problem, I used a dummy node and left/right pointers. The dummy node is used to handle the case when we need to remove the head node. There are exactly n spaces between the left node and the right node at the end of the list. Once we have a pointer to the prev node n slots away from the end of the list, we can just set left = left.next.next. Now we can return the dummy node. 

- Time complexity O(n) 
- Space complexity O(1)

```python
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Create a dummy node if we need to remove the head
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Move right pointer n steps ahead
        for i in range(n):
            right = right.next
        
        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next

        # Remove the nth node from the end
        left.next = left.next.next

        return dummy.next
```