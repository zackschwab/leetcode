# 28. Index of the First Occurrence in a String

[Link](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        for i in range(len(haystack) - len(needle) + 1):
            match = True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i

        return -1
```