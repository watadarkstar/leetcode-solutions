"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        m = len(nums) - k
        self.reverse(nums, 0, m - 1)
        self.reverse(nums, m, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)
        
    def reverse(self, nums, i, j):
        """
        :type nums: List[int]
        :type i: int (starting index at 0)
        :type j: int (end index)
        :rtype void
        """
        while i < j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
            j -= 1
