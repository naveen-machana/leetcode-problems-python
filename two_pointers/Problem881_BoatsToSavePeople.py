'''
https://leetcode.com/problems/boats-to-save-people/
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where
each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum
of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
'''
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        st, end = 0, len(people) - 1
        res = 0
        while st <= end:
            if people[st] + people[end] <= limit:
                st += 1
            end -= 1
            res += 1
        return res