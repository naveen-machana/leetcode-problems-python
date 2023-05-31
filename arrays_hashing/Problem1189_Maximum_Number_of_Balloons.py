'''
https://leetcode.com/problems/maximum-number-of-balloons/
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.
Input: text = "nlaebolko"
Output: 1
Input: text = "loonbalxballpoon"
Output: 2

balloon          = [1,1,2,2,1]
loonbalxballpoon = [4,4,2,2,2]
'''
import collections
from collections import Counter

class Solution:
    # brute-force approach
    def maxNumberOfBalloons2(self, text: str) -> int:
        balloon_count = collections.defaultdict(int)
        for c in 'balloon':
            balloon_count[c] += 1
        str_chars = collections.defaultdict(int)
        for c in text:
            str_chars[c] += 1
        res = 0
        while True:
            for c in balloon_count:
                if c not in str_chars or str_chars[c] < balloon_count[c]:
                    return res
                str_chars[c] -= balloon_count[c]
            res += 1

    def maxNumberOfBalloons2(self, text: str) -> int:
        countText = Counter(text)
        balloon = Counter('balloon')
        res = len(text) # or float('inf')

        for c in balloon:
            res = min(res, countText[c] // balloon[c])
        return res