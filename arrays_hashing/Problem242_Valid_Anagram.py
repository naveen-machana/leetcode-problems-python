'''
https://leetcode.com/problems/valid-anagram/
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true
'''
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCount, tCount = collections.defaultdict(int), collections.defaultdict(int)
        for i in range(len(s)):
            sCount[s[i]] += 1
            tCount[t[i]] += 1

        return sCount == tCount