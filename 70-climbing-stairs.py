"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {0: 0, 1: 1, 2: 2}
        
        if n in dp:
            return dp[n]
        
        for i in range(2,n):
            dp[i + 1] = dp[i] + dp[i - 1]
            
        return dp[n]
