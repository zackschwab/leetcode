# 88 Merge sorted array
[Link](https://leetcode.com/problems/merge-sorted-array/description/)


For this problem, I used a left and right pointer to split the array in half after each iteration of the loop. I thought of it as searching for a page in a book where each iteration, we find the midpoint and compare the midpoint to the target. If the midpoint is greater than the left page, we know that we can get rid of everything to the left by setting the left pointer to midpoint + 1. If the left pointer ever passes the right pointer, we need to return the left pointer since the target wasn't found and now the right pointer is in an incorrect spot.

- Time complexity O(logn) 
- Space complexity O(1)

```python

            
```