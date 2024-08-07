'''
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

'''
import collections


class Solution(object):
    def countCharacters(self, words, chars):
        charsCounter = collections.Counter(chars)
        res = 0
        for word in words:
            good = True
            wcounter = collections.defaultdict(int)
            for c in word:
                wcounter[c] += 1
                if c not in charsCounter or wcounter[c] > charsCounter[c]:
                    good = False
                    break
            if good:
                res += len(word)

        return res
