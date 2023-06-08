'''
https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
A palindrome is a string that reads the same forwards and backwards.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted
 without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
'''

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        chars = set(s)
        for char in chars:
            st, end = s.find(char), s.rfind(char)
            res += len(set(s[st + 1 : end]))
        return res