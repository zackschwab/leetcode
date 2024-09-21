# 71 Simplify Path
[Link](https://leetcode.com/problems/search-insert-position/?envType=study-plan-v2&envId=top-interview-150)


For this problem, I split the path into multiple substrings by "/". Then, I iterated through each string in the directories array. If the directory is empty, this means there was an unnecessary slash, and if it is a '.', we can simply ignore it. Then, I checked for '..' and if one is found, we need to pop the recent directory from the stack. Finally, at the end of the loop we know the directory is valid so we can append it to the stack. Once the loop finishes, we can join each directory in the stack and separate them with a '/' to get the simplified path

- Time complexity O(n) 
- Space complexity O(n)

```python
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        stack = []

        directories = path.split("/")
        for d in directories:
            # If directory is empty, there was an unnecessary /. Also check for . since we don't do anything
            if not d or d == '.':
                continue
            
            if d == '..':
                # Pop the recent directory from the stack if it isn't empty
                if stack:
                    stack.pop()
                else:
                    # If stack is empty, don't do anything since we can't go above root directory
                    continue
            else:
                # The current directory is valid so add it to the stack
                stack.append(d)

        # Stack now contains the valid directory structure, so join each string with a / in between
        path = '/' + '/'.join(stack)
        
        return path         
```