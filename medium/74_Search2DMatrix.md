# 74. Search 2D Matrix  
[Link](https://leetcode.com/problems/search-a-2d-matrix/description/?envType=study-plan-v2&envId=top-interview-150)


For this problem, I used binary search twice. First, I used binary search to find which row contains the target value by comparing the largest and smallest values at midRow and updating the top/bot pointers. When I found the row, I used binary search with left and right pointers, returning true if the target is ever found. If the second loop finishes without returning true, the value wasn't found so we can return false.

- Time complexity O(log(m * n)) 
- Space complexity O(1)

```python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        # We need to find the row index w/ binary search
        top = 0
        bot = len(matrix) - 1
        row = 0

        while top <= bot:
            midRow = (top + bot) // 2
            
            if matrix[midRow][0] > target:
                bot = midRow - 1
            elif matrix[midRow][-1] < target:
                top = midRow + 1
            else: 
                break

        row = (top + bot) // 2
        if top > bot:
            return False
        
        # Use binary search to find target in row
        left = 0
        right = len(matrix[row]) - 1
        
        while left <= right:
            midpoint = (left + right) // 2
            currVal = matrix[row][midpoint]

            if currVal > target:
                right = midpoint - 1
            elif currVal < target:
                left = midpoint + 1
            else:
                # We found the target
                return True
                
        # Target does not exist in matrix
        return False
```