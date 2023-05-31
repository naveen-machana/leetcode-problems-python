'''
https://leetcode.com/problems/word-pattern/
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sstrs = s.split()
        if len(sstrs) != len(pattern):
            return False
        fwd, rev = {}, {}
        for a, b in zip(pattern, sstrs):
            if (a in fwd and fwd[a] != b) or (b in rev and rev[b] != a):
                return False
            fwd[a] = b
            rev[b] = a
        return True