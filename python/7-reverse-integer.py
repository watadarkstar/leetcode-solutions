"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            num = -1*int(str(-1*x)[::-1])
        else:
            num = int(str(x)[::-1])
        
        if num < -2147483647 or num > 2147483647:
            return 0
        else:
            return num
