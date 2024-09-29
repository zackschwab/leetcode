# 69. Sqrt(X)
[Link](https://leetcode.com/problems/sqrtx/?envType=study-plan-v2&envId=top-interview-150)


For this problem, I used binary search. Each iteration, I compared the midpoint^2 to the target value, x until we find the sqrt.

- Time complexity O(logn)
- Space complexity O(1)

```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        left = 0
        right = x

        # Edge case for x = 0, 1
        if x < 2:
            return x

        while left <= right:
            midpoint = (left + right) // 2
            square = midpoint * midpoint

            if square == x:
                return midpoint
            elif square < x:
                left = midpoint + 1
            else:
                right = midpoint - 1

        # When the loop ends, right will be the integer part of the square root
        return right
```