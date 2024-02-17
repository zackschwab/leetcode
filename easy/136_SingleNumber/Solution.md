# 136. Single Number

[Link](https://leetcode.com/problems/single-number/?source=submission-ac)

To solve this problem, I decided to use a dictionary. First, I incremented through the array of numbers, created a key for each number, and incremented the value

Then, I checked the whole dictionary to find the value with a key of 1, which is constant time.

-Time complexity: O(n)
-Space complexity: O(n).


```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = dict()

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        for num, frequency in count.items():
            if frequency == 1:
                return num
```

# Better Solution
The better solution for this problem is to use XOR bit manipulation. Prior to this problem, I was unaware that XORing an array by 0 would result in each number being canceled out besides the value that appears once. This solution results in:

-Time complexity: O(n)
-Space complexity: O(1)

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        
        return xor
```