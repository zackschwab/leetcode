# 345. Reverse Vowels of a String
[Link](https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75)


For this problem, I used a two pointer approach where the left pointer keeps track of the current left vowel and the right one keeps track of the right vowel. During each loop, we need to check if the left pointer and right pointers are on a vowel. If the left one isn't, increment it and for the right, decrement it. If they are equal, we need to swap the two vowels to reverse them. Once the left pointer is greater than the right pointer, this means the pointers have met so if the loop continues we will effectively un-reverse the string. I used a list of characters since python strings are immutable and I used a set to look up the vowels.

- Time complexity O(n) 
- Space complexity O(n)

```python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        left = 0
        right = len(s) - 1
        string = list(s)
        vowels = set('aeiou')

        while left < right:
            if s[left].lower() in ['a', 'e', 'i', 'o', 'u'] and s[right].lower() in ['a', 'e', 'i', 'o', 'u']:
                # If both pointers are on a vowel, swap them
                temp = string[left]
                string[left] = string[right]
                string[right] = temp
                left += 1
                right -= 1

            if s[left].lower() not in vowels:
                left += 1

            if s[right].lower() not in vowels:
                right -= 1

        return ''.join(string)                 
```