'''
https://leetcode.com/problems/longest-common-prefix/
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
from typing import List


class Solution:
    # approach 2
    # compare first and second strings, get common prefix
    # use the common prefix to compare with 3rd string, get common prefix
    # use that for comparing with 4th string, get common prefix,
    # repeat the process
    def longestCommonPrefix_2(self, strs: List[str]) -> str:
        prev = strs[0]
        for i in range(len(strs) - 1):
            next = ""
            for j in range(min(len(prev), len(strs[i + 1]))):
                if prev[j] == strs[i + 1][j]:
                    next = next + prev[j]
                else:
                    break
            prev = next
        return prev

    # compare characters of first string with characters from other strings
    # fail fast as soon as there is a difference
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res