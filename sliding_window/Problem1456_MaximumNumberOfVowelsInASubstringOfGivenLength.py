'''
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        l, res, cur = 0, 0, 0
        for r, c in enumerate(s):
            cur += 1 if c in vowels else 0
            if r - l + 1 > k:
                cur -= 1 if s[l] in vowels else 0
                l += 1
            res = max(res, cur)
        return res