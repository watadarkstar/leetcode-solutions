/** 242. Valid Anagram
 *
 * Given two strings s and t, write a function to determine if t is an anagram of s.
 *
 * For example,
 * s = "anagram", t = "nagaram", return true.
 * s = "rat", t = "car", return false.
 *
 * Note:
 * You may assume the string contains only lowercase alphabets.
 *
 * Follow up:
 * What if the inputs contain unicode characters? How would you adapt your solution to such case?
 */

public class Solution {
    /** O(N) Time Complexity, O(N) Space Complexity Solution
     *
     * Steps:
     * 1. Convert string `s` into a hashmap of character counts 
     * 2. Decrement count for each character in string `t` that is found in hashmap 
     *    Note: If character not found in hashmap return false, else if decrement
     *          causes count to reach 0 remove key from hashmap
     * 3. Return whether hashmap has been completely matched by characters in t
     */

    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> hm = new HashMap<Character, Integer>();
        
        
        for (char c : s.toCharArray()) {
            hm.put(c, hm.getOrDefault(c, 0) + 1);
        }
        
        for (char c : t.toCharArray()) {
            if (hm.containsKey(c)) {
                int i = hm.get(c);
                i -= 1;
                if (i == 0) {
                    hm.remove(c);
                } else {
                    hm.put(c, i);
                }
            } else {
                return false;
            }
        }
    
    	return hm.isEmpty();	
    }
}
