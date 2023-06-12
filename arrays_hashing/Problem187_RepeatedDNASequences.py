import collections
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, dup = set(), set()
        for i in range(len(s) - 9):
            current = s[i : i + 10]
            if current in seen:
                dup.add(current)
            seen.add(current)
        return list(dup)