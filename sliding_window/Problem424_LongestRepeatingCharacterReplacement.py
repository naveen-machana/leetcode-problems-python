'''
https://leetcode.com/problems/longest-repeating-character-replacement/description/
You are given a string s and an integer k. You can choose any character of the string and change it to any other
uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counters = [0] * 26
        l, res = 0, 0
        for r in range(len(s)):
            counters[ord(s[r]) - ord('A')] += 1
            while (r - l + 1 - max(counters)) > k:
                counters[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res