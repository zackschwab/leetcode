# 141 LinkedListCycle
[Link](https://leetcode.com/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150)

To solve this problem, I iterated through the linked list until the nextNode was null. Each iteration, check if the current node is in our hash table of nodes and if it isn't, add the currNode to the hash table. If the current node is found in the hash table, we can return true and if the loop finishes executing without finding a duplicate, return false. 

- Time Complexity: O(n) since we used a hash table 
- Space complexity: O(n) since we used a hash table

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vals = {}
        currNode = head

        while currNode:
            if vals.get(currNode):
                return True
            
            vals[currNode] = 1
            currNode = currNode.next
```            

# Another solution
Instead of using a hash table to store each node, we can use the tortoise and hare algorithm. This algorithm uses a slow pointer and a fast pointer. The slow pointer iterates through the list one node at a time and the fast pointer iterates two nodes at a time. If the fast pointer and slow pointer ever meet, there must be a cycle. 

- Time complexity: O(1)
- Space complexity: O(1) since we don't need to create a hash table 

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow =  slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False          
```