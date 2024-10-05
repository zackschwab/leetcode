# 66. Plus One
[Link](https://leetcode.com/problems/plus-one/description/?envType=study-plan-v2&envId=top-interview-150)


For this problem, I started at the end of the array and checked if each number in the array is 9 (since 10 needs two digits). If it is, set the current element to zero, carry the one, and continue this process with the previous element. If we reach the end of the array (curr <= 0), the most significant digit needs to be 1, and we can append a zero to the end. 

- Time complexity O(n)
- Space complexity O(1)

```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        curr = len(digits) - 1

        while curr >= 0:
            if digits[curr] == 9:
                digits[curr] = 0
                curr -= 1
            else:
                digits[curr] += 1
                return digits
        
        digits[0] = 1
        digits.append(0)
        return digits
```