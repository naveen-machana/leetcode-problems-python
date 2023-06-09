'''
https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/
Given a string s, find two disjoint palindromic subsequences of s such that the product of their lengths is maximized.
The two subsequences are disjoint if they do not both pick a character at the same index.
Return the maximum possible product of the lengths of the two palindromic subsequences.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing
the order of the remaining characters. A string is palindromic if it reads the same forward and backward.

Input: s = "leetcodecom"
Output: 9
Explanation: An optimal solution is to choose "ete" for the 1st subsequence and "cdc" for the 2nd subsequence.
The product of their lengths is: 3 * 3 = 9.
'''

class Solution:
    def maxProduct(self, s: str) -> int:
        pali, N = {}, len(s)
        for mask in range(1, 1 << N):
            subseq = ""
            for i in range(N):
                if mask & (1 << i) != 0:
                    subseq = s[i] + subseq
            if subseq == subseq[::-1]:
                pali[mask] = len(subseq)

        res = 0
        for i in pali:
            for j in pali:
                if i & j == 0:
                    res = max(res, pali[i] * pali[j])

        return res