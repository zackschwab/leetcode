# 206 Reverse Linked List

[Link](https://leetcode.com/problems/reverse-linked-list/)

To solve this problem, I used a three pointer approach. The curr pointer points to the current node in the list, prev points to the previous node, and temp stores the curr node so we can reverse the link between each node. Curr is initialized to head, prev and temp are initialized to null. Then, iterate through the loop until curr is null. Each iteration, we store the current next node in temp and then set curr.next = prev, then prev = curr and curr = temp. This effectively reverses the link between the nodes and once the loop finishes, the prev pointer will be the head of our reversed linked list. 

- Time complexity: O(n) we have to iterate through the list once
- Space complexity O(1) no additional data structures are used

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        curr = head
        prev = None
        temp = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
```


### TODO
- Add a recursive approach