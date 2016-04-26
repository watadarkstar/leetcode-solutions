/* 137. Single Number II
 * Given an array of integers, every element appears three except for one. Find that single one.
 *
 * Note:
 * Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
 */

public class Solution {
    public int singleNumber(int[] nums) {
        /* Idea Explanation:
         *      1. Represent the list of integers in binary form.
         *      2. Count the number of times each bit appears in 
         *         the list in each of the 32 possible placements.
         *      3. Modulo 3 each of these counts to get a binary
         *         number that is the number appearing exactly once. */
        int counterOne = 0;
        int counterTwo = 0;
        int prevCounterOne = 0;
        
        for (int i = 0; i < nums.length; i++) {
            counterOne = (counterOne & ~nums[i]) | (~counterTwo & ~counterOne & nums[i]);
            counterTwo = (counterTwo & ~nums[i]) | (prevCounterOne & nums[i]);
            prevCounterOne = counterOne;
        }
        return counterOne;
    }
}
