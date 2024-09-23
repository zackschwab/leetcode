# 374. Guess Number Higher or Lower
[Link](https://leetcode.com/problems/guess-number-higher-or-lower/?envType=study-plan-v2&envId=leetcode-75)


For this problem, I used binary search. 

- Time complexity O(logn) 
- Space complexity O(1)

```python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        left = 1
        right = n

        while left < right:
            midpoint = (left + right) // 2
            result = guess(midpoint)
            
            if result == 0:
                return midpoint
            if result == -1:
                # If our guess is higher, we need to look at smaller numbers
                right = midpoint - 1
            else:
                # Our guess is lower
                left = midpoint + 1

        return left                      
```