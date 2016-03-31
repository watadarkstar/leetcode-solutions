class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, n in enumerate(nums):
            diff = target - n
            if n in d:
                return [d[n], i]
            else:
                d[diff] = i
        return False
