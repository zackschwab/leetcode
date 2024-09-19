# 88 Merge sorted array
[Link](https://leetcode.com/problems/merge-sorted-array/description/)


For this problem, since the last n elements of the array are filled with zeroes, we can start from the end of nums1 array. I started from the end and added the largest element from either nums1 or nums2. When the loop finishes, the array is either sorted, or nums2 has more smaller numbers. Now we need to loop until n <= 0 to account for this case. 

- Time complexity O(m + n) 
- Space complexity O(1)

```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # Indices start at 0
        m -= 1
        n -= 1
        curr = m + n - 1


        # Start at last element in array until one of the pointers is less than 0
        while m > 0 and n > 0:
            if nums1[m] > nums2[n]:
                nums1[curr] = nums1[m]
                m -= 1
            else:
                nums1[curr] = nums2[n]
                n -= 1
            curr -= 1

        # If n > 0, we need to fill the remaining slots
        while n > 0:
            nums1[curr] = nums2[n]
            n -= 1
            curr -= 1
            
```