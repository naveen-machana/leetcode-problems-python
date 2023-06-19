'''
https://leetcode.com/problems/valid-palindrome/
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''
class Solution:
    def isPalindrome1(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()

        return newStr == newStr[::-1]

    def isPalindrome(self, s: str) -> bool:

        def alphanumeric(char):
            return (ord('a') <= ord(char) <= ord('z') or
                    ord('A') <= ord(char) <= ord('Z') or
                    ord('0') <= ord(char) <= ord('9'))

        st, end = 0, len(s) - 1
        while st < end:
            while st < end and not alphanumeric(s[st]): st += 1
            while st < end and not alphanumeric(s[end]): end -= 1
            if s[st].lower() != s[end].lower():
                return False
            st, end = st + 1, end - 1
        return True







