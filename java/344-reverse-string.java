/* 344. Reverse String
 *
 * Write a function that takes a string as input and returns the string reversed.
 *
 * Example:
 * Given s = "hello", return "olleh".
 */

public class Solution {
    public String reverseString(String s) {
        int strLen = s.length();
        char[] charArray = s.toCharArray();
        char[] retCharArray = new char[strLen];
        
        for(int i = 0; i < strLen; i++) {
            retCharArray[strLen-i-1] = charArray[i];
        }
        return new String(retCharArray);
    }
}