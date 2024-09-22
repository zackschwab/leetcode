# 392 Is Subsequence
[Link](https://leetcode.com/problems/search-insert-position/?envType=study-plan-v2&envId=top-interview-150)


For this problem, I used a two pointer approach to iterate through the entire string t. During each iteration, we check if the current value in t is equal to the current value in s and if they are, we increment s. The t pointer will always be incremented. After the loop finishes executing, we can check the index of s to determine if we successfully found a subsequence. If the index of s == len(s), we know that each character was able to find a match. 

- Time complexity O(n) 
- Space complexity O(1)

```python
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s_ptr = 0
        t_ptr = 0

        while t_ptr < len(t) and s_ptr < len(s):
            s_char = s[s_ptr]
            t_char = t[t_ptr]

            # If we find a match we can increment the s_ptr
            if s_char == t_char:
                s_ptr += 1

            # t_ptr will always be incremented
            t_ptr += 1

        # If s_ptr == len(s), each character in s was successfully found in t in order
        if s_ptr == len(s):
            return True

        return False                         
```