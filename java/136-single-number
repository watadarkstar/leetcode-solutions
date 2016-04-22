/* 136. Single Number
 * Given an array of integers, every element appears twice except for one. Find that single one.
 *
 * Note:
 * Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
 * 
 * Subscribe to see which companies asked this question
 */

public class Solution {
    public int singleNumber(int[] nums) {
        /* Idea Explanation:
         *      1. Represent the list of integers in binary form.
         *      2. Count the number of times each bit appears in 
         *         the list in each of the 32 possible placements.
         *      3. Modulo 2 each of these counts to get a binary
         *         number that is the number appearing exactly once. */
        int counter = 0;
        
        for (int i = 0; i < nums.length; i++) {
            // Note: This can be better represented by an XOR, it has been
            //       left as is too indicate a Karnaugh Map had been used
            //       to get the result.
            counter = (~counter & nums[i]) | (counter & ~nums[i]);
        }
        return counter;
    }
}
