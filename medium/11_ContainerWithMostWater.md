# 11. Container with Most Water
[Link](https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150)


For this problem, I used a left and right pointer to point to the tallest heights on each side. I start with the left pointer at 0, and right pointer at n - 1, and shift the smallest pointer towards the middle each iteration. I also keep track of the maxWater found by initializing it to 0, and each iteration we calculate the currWater by multiplying the width (left - right) by the height of the current container (the smallest of the two heights since water will overflow).

- Time complexity O(n)
- Space complexity O(1)

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(height) - 1
        maxWater = 0

        while left < right:
            # Calculate currWater by multiplying width * smallest height
            currHeight = min(height[left], height[right])
            currWater = (right - left) * currHeight

            if currWater > maxWater:
                maxWater = currWater

            # Shift the smallest pointer towards the middle
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                # If they are equal, we can shift the left pointer
                left += 1
        
        return maxWater
```