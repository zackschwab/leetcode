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
