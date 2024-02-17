# 169 Majority Element
[Link](https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150)

To solve this problem, I created a dictionary/hash table where the key represents each number in the array and the value represents the total number of occurrences. First, I iterated through the array and if the value wasn't in the dictionary, I would add it and set its value to 1. If it was found, increment the value. Next, I used the max function to find the key with the greatest value. 

- Time Complexity: O(n) since we used a hash table 
- Space complexity: O(n) since we used a hash table

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        vals = dict()

        for num in nums:
            if num not in vals:
                vals[num] = 1
            else:
                vals[num] += 1

        return max(vals, key=vals.get)
```

# Another solution
Instead of using a hash table, we can also sort the array and then find the value stored at n // 2 (since the midpoint will contain the majority element). Python uses the Timsort algorithm which has a time complexity of O(nlogn). 

- Time complexity: O(nlogn)
- Space complexity: O(1) since we don't need to create a hash table 

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) // 2]
```