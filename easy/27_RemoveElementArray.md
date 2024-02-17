# 27 Remove Element from Array

For this problem, I used a two pointer approach
- left represents left pointer 
- right represents right pointer

We want to iterate through the array until left > right and check if the current value in the left pointer is equal to the target value. If they are equal, swap the element from the right pointer with the left pointer to get rid of it. Now decrement the right pointer. If the left value isn't equal to target val, then we simply increment left and right remains the same. 

- Time complexity O(n) 
- Space complexity O(1)

```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1

        return left
```