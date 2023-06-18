'''
https://leetcode.com/problems/naming-a-company/
You are given an array of strings ideas that represents a list of names to be used in the process of naming a company.
The process of naming a company is as follows:

Choose 2 distinct names from ideas, call them ideaA and ideaB.
Swap the first letters of ideaA and ideaB with each other.
If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and
ideaB, separated by a space) is a valid company name.
Otherwise, it is not a valid name.
Return the number of distinct valid names for the company.

Input: ideas = ["coffee","donuts","time","toffee"]
Output: 6
Explanation: The following selections are valid:
- ("coffee", "donuts"): The company name created is "doffee conuts".
- ("donuts", "coffee"): The company name created is "conuts doffee".
- ("donuts", "time"): The company name created is "tonuts dime".
- ("donuts", "toffee"): The company name created is "tonuts doffee".
- ("time", "donuts"): The company name created is "dime tonuts".
- ("toffee", "donuts"): The company name created is "doffee tonuts".
Therefore, there are a total of 6 distinct company names.

The following are some examples of invalid selections:
- ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
- ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
- ("coffee", "toffee"): Both names formed after swapping already exist in the original array.

Input: ideas = ["lack","back"]
Output: 0
Explanation: There are no valid selections. Therefore, 0 is returned.
'''
import collections
from typing import List

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        wordMap = collections.defaultdict(set)
        for idea in ideas:
            wordMap[idea[0]].add(idea[1:])

        res = 0
        for word1 in wordMap:
            for word2 in wordMap:
                if word1 == word2:
                    continue

                intersect = 0
                for suffix in wordMap[word1]:
                    if suffix in wordMap[word2]:
                        intersect += 1

                distinct1 = len(wordMap[word1]) - intersect
                distinct2 = len(wordMap[word2]) - intersect
                res += (distinct1 * distinct2)

        return res