'''
https://leetcode.com/problems/merge-strings-alternately/
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
 If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i, j, m, n = 0, 0, len(word1), len(word2)
        while i < m or j < n:
            if i < m: res += word1[i]
            if j < n: res += word2[j]
            i, j = i + 1, j + 1
        return res