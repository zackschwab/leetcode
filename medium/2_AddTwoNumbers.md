# 2. Add 2 Numbers  
[Link](https://leetcode.com/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150)

For this problem, I used a stack to store the digits of each linked list. We can get the two numbers by popping from the stack and add them together to find the correct sum. Now, we can create a new linked list starting from the end of our new string to make the linked list in reverse order. 

- Time complexity O(m + n) where m is numDigits in l1 and n is numDigits in l2
- Space complexity O(m + n)

```python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        stack1 = []
        stack2 = []
        
        # Traverse the lists and push the digits into stack
        currNode1 = l1
        while currNode1:
            stack1.append(currNode1.val)
            currNode1 = currNode1.next
        
        currNode2 = l2
        while currNode2:
            stack2.append(currNode2.val)
            currNode2 = currNode2.next

        nums1 = ""
        nums2 = ""
        
        # Get the number in correct order by popping from stack
        while stack1:
            nums1 += str(stack1.pop())

        while stack2:
            nums2 += str(stack2.pop())
        
        sumValue = int(nums1) + int(nums2)
        sumString = str(sumValue)

        # Create the first digit in the linked list
        sumList = ListNode(int(sumString[-1]))
        currNode = sumList
        
        # Add remaining digits to the linked list in reverse order
        for i in range(len(sumString) - 2, -1, -1):
            newNode = ListNode(int(sumString[i]))
            currNode.next = newNode
            currNode = currNode.next

        return sumList
```

# TODO
Optimize this using addition and carry digits