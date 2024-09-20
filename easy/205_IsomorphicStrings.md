# 205. Isomorphic Strings
[Link](https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150)

To solve this problem, we need to map each character in the first string to the corresponding character in the second one. I used two hash maps since we need to map them in each direction. Next, I looped through the strings and checked if each character has a mapping. If a character has a mapping but it doesn't match the expected character in the other string, return false. If we reach the end of the loop, the current character must be a new entry so we need to map the characters in each hash table. 

- Time complexity: O(n) since we only iterate through the strings once
- Space complexity: O(n) since we use two hash tables of length n

```python
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # We need 2 hash maps to map characters from s -> t and t -> s
        map_s = {}
        map_t = {}

        # Strings cannot be isomorphic if they have different length
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            # Check if there is a correct mapping for both directions
            if s[i] in map_s and map_s.get(s[i]) != t[i]:
                return False
            
            if t[i] in map_t and map_t.get(t[i]) != s[i]:
                return False

            # Create a new record in each hash map
            map_s[s[i]] = t[i]
            map_t[t[i]] = s[i]
        
        # If we made it through the loop, they are isomorphic
        return True
```