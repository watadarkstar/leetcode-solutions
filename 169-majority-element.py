"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = [nums[0], 1]
        
        for n in nums[1:]:
            if majority[1] == 0:
                majority[0] = n
                majority[1] = 1
            elif majority[0] == n:
                majority[1] += 1
            else:
                majority[1] -= 1
            
        return majority[0]
