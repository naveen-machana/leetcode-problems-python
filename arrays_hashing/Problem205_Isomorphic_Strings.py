'''
https://leetcode.com/problems/isomorphic-strings/description/
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true

Input: s= "badc", t = "baba"
Output: false
'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        fwd, rev = {}, {}
        for i in range(len(s)):
            if fwd.get(s[i], t[i]) != t[i] or rev.get(t[i], s[i]) != s[i]:
                return False

            fwd[s[i]] = t[i]
            rev[t[i]] = s[i]
        return True
