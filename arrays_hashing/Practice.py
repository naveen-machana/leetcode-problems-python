from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += (len(s) + '#' + s)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # 4#neet
            hashIndex = s.index('#', i)
            length = int(s[i : hashIndex])
            substr = s[hashIndex + 1 : hashIndex + length]
            res.append(substr)
            i = hashIndex + length
        return res
