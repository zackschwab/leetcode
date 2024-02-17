# 26 Remove Duplicates from Sorted Array
[Link](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150)

To solve this problem, I decided to use a two pointer approach. 
- K represents the left pointer and number of distinct elements
- i represents the right pointer, which searches through the array to find the next largest number

First, initialize k to 1, since we know that the first element will be unique. Next, we need to traverse the array to find the next distinct number using i. Once we find a new distinct number, set the value in nums[k] = i. This will give us an array where the first k elements contain the sorted array, and each element after can be disregarded. 

For this problem, they want us to return k, and we don't need to return the array since it was already modified. The caller can now use the values 0-k in the array. 

- Time complexity: O(n) we only need to traverse the array once
- Space complexity: O(1) since we modify the array directly instead of allocating memory to create a new one

```python 
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        k = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                nums[k] = nums[i]
                k += 1
            

        return k
```