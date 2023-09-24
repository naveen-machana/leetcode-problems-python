'''
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, return the minimum window substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring,
 return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

'''
from collections import Counter
from math import inf


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        left, matches, minLength = 0, 0, float(inf)
        minWindow = ''

        sCounter = Counter()
        for right, c in enumerate(s):
            sCounter[c] += 1
            if c in target and sCounter[c] == target[c]:
                matches += 1

            while matches == len(target):
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    minWindow = s[left : right + 1]

                leftChar = s[left]
                sCounter[leftChar] -= 1

                if leftChar in target and sCounter[leftChar] < target[leftChar]:
                    matches -= 1

                left += 1

        return minWindow