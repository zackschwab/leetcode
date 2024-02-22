# 1 Two Sum 

[Link](https://leetcode.com/problems/two-sum/)

To solve this problem, I used a two pointer approach. The left pointer represents the left pointer in the list, and the right pointer represents the right pointer in the list. I used a nested for loop where the left starts at 0 and iterates through the whole list. The second loop is for the right pointer, which always starts at left + 1. Each iteration of the second for loop, we check if the sum of nums[left] == nums[right]. If so, return [left, right]. If a match is not found, return [-1, -1]

Time complexity: O(n^2) since we have a nested for loop

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                if nums[left] + nums[right] == target:
                    return [left, right]
            
        return [-1, -1]
```

# A better solution
Instead of the brute force approach, we can use a hash map and arithmetic to achieve linear time complexity. First, I initialized a hash map, then we can iterate through the list. Each time we iterate, we calculate the difference between nums[i] and target, and this will give us the number we need. Now, we can search the hash map for a match, since the hash map can search the whole array in constant time. If we don't find a match, add an entry, along with its index, to the hash map and continue through the loop. 

Time complexity: O(n) since we only need to iterate through the array once in the worst case. 

```python
 def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #value, index
        map = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in map:
                return [i, map.get(diff)]
            else:
                map.update({nums[i]: i})
```