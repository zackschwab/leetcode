# 61. Rotate Linked List
[Link](https://leetcode.com/problems/guess-number-higher-or-lower/?envType=study-plan-v2&envId=leetcode-75)


For this problem, I traversed the linked list to find the size and get a pointer to the tail of the linked list. Next, I used the size to traverse the linked list (size % k) - 1 times to find the new head element and a pointer to the node before it. Keep in mind, if k is divisible by the size, that means that you aren't actually rotating the array since the new head we find will be the same head. To create the new linked list, we have to remove the link between newHead and prev. Next, we have to set the tail to the old head to reconnect the list.  

- Time complexity O(n) 
- Space complexity O(1)

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        tail = head
        size = 1

        newHead = head
        prev = head
        
        if not head:
            return head

        # Traverse the list to find the length and tail
        while tail.next:
            tail = tail.next
            size += 1
        
        # If k is divisible by the size of the list, rotating it won't do anything
        if k % size == 0:
            return head

        # Find the head and prev node
        for i in range(size - k % size):
            prev = newHead
            newHead = newHead.next
        
        # Get rid of the elements to the left of new head
        prev.next = None

        # Set the tail to the old head to connect the rest of the list
        tail.next = head
        head = newHead

        return head                      
```