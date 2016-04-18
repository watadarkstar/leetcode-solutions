"""
Given an integer, write a function to determine if it is a power of two.

**STUDY** = know why this is true in the binary
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & n-1)