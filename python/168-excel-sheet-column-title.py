"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 

**STUDY**
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        sol = ""
        
        while n > 0:
            chrCode = 26 if n % 26 == 0 else n % 26
            sol = chr(chrCode + 64) + sol
            n = n - chrCode
            n /= 26
            
        return sol
