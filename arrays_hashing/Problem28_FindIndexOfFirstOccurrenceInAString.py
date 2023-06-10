'''
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = self.lps(needle)
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
                if j == len(needle):
                    return i - j
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
        return -1

    def lps(self, needle: str):
        lps, n = [0] * len(needle), len(needle)
        i, j = 0, 1
        while j < n:
            if needle[j] == needle[i]:
                lps[j] = i + 1
                j, i = j + 1, i + 1
            else:
                if i == 0:
                    lps[j] = 0
                    j += 1
                else:
                    i = lps[i - 1]
        return lps