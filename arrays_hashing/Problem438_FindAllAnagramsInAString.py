'''
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in
any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
using all the original letters exactly once.
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
'''
import collections
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCount, sCount = [0] * 26, [0] * 26
        for c in p:
            pCount[ord(c) - ord('a')] += 1

        res = []
        for i, c in enumerate(s):
            sCount[ord(c) - ord('a')] += 1
            if i - len(p) >= 0:
                sCount[ord(s[i - len(p)]) - ord('a')] -= 1
            if sCount == pCount:
                res.append(i + 1 - len(p))
        return res
