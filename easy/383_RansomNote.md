# 383. Ransom Note

[Link](https://leetcode.com/problems/ransom-note/)

To solve this problem, I used a hash map containing each character in magazine, where key represents the character and value represents # of occurrences. Next, I iterated through each character in ransomNote and checked if the character is in my hash map and the value is greater than 0. If it is, decrement the value. If it isn't return false. Once we finish the for loop, we can return true. 

Time complexity: O(n + m)
Space complexity: O(n) 

```python
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        chrs = {}

        for ch in magazine:
            if ch not in chrs.keys():
                chrs.update({ch : 1})
            else:
                chrs.update({ch : chrs.get(ch) + 1})
        
        for ch in ransomNote:
            if ch not in chrs.keys() or chrs.get(ch) <= 0:
                return False

            chrs.update({ch : chrs.get(ch) - 1})

        return True
```