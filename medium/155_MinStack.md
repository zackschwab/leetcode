# 155. Min Stack  
[Link](https://leetcode.com/problems/min-stack/description/?envType=study-plan-v2&envId=top-interview-150)


For this problem, I designed the min stack with a python list to store each value in the stack in order, and I also used a stack to store the min values in order. For the push method, we need to add the value to the main stack, but we only have to add it to the minStack if its lower than our current min value. If we pop a entry from the stack, we need to remove it from the main stack and also check if it is equal to our current minVal in our min stack, popping if necessary. We can always get the min value in constant time by returning the last entry in our min list. 

- Time complexity O(1) 
- Space complexity O(n)

```python
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val) 
        
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)  

    def pop(self):
        """
        :rtype: None
        """
        top_val = self.stack.pop() 
        
        if top_val == self.min_stack[-1]:
            self.min_stack.pop()       

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```