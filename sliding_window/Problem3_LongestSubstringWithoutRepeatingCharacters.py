'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string s, find the length of the longest substring without repeating characters.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexMap = {}
        res, st = 0, 0
        for i, c in enumerate(s):
            if c in indexMap:
                st = max(st, indexMap[c] + 1)
            res = max(res, i - st + 1)
            indexMap[c] = i
        return res

