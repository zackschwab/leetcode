# 20 Valid Parenthesis
[Link](https://leetcode.com/problems/valid-parentheses/description/)

For this problem, I decided to use a stack data structure. First, I created an empty stack and then I created a list containing each opening bracket, and a list containing each closing bracket. Next, we have to iterate through the string and if the character is an opening bracket, we push it to the stack. If the character is a closing bracket, first we need to make sure the list isn't empty, then we need to check if the closing bracket matches the opening bracket. To achieve this, I used the index of the character in the list and made sure the corresponding brackets indices match. 

Once we iterate through the entire string, all we need to do is make sure the stack is empty. If the stack is not empty, then the first opening bracket was never closed, so we have to return false. Otherwise return true. 

Time complexity -- O(n), where n represents length of string, since we have to iterate through the entire string once.

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        opening = ['(', '[', '{']
        closing = [')', ']', '}']

        for ch in s:
            if ch in opening:
                stack.append(ch)
            else:
                if not stack or closing.index(ch) != opening.index(stack.pop()):
                    return False
            
        return not stack
```


# Better Solution
Instead of using two lists, I should have used a hashmap to optimize space and time complexity since we have to search through my two lists multiple times. 

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map.keys():
                if not stack or stack.pop() != bracket_map[char]:
                    return False
            else:
                return False
        
        return not stack

```