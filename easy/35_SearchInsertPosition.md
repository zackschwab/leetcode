# 35 Search Insert Position
[Link](https://leetcode.com/problems/search-insert-position/?envType=study-plan-v2&envId=top-interview-150)


For this problem, I used binary search with a left and right pointer to split the array in half after each iteration of the loop. I thought of it as searching for a page in a book where each iteration, we find the midpoint and compare the midpoint to the target. If the midpoint is greater than the left page, we know that we can get rid of everything to the left by setting the left pointer to midpoint + 1. If the left pointer ever passes the right pointer, we need to return the left pointer since the target wasn't found and now the right pointer is in an incorrect spot.

- Time complexity O(logn) 
- Space complexity O(1)

```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left = 0
        right = len(nums) - 1

        # Continue until the left pointer goes past or equals the left pointer 
        while left <= right:
            # Find the midpoint
            midpoint = (right + left) // 2

            # We found the index
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                # Get rid of the entries to the left of midpoint
                left = midpoint + 1
            else:
                # Get rid of entries to the right of midpoint
                right = midpoint - 1
        
        # After the loop finishes, if the target wasn't found, return the left pointer
        return left
            
```