from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append('#')
            encoded.append(s)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            hashIndex = s.index('#', i)
            charsCtr = int(s[i : hashIndex])
            res.append(s[hashIndex + 1 : hashIndex + 1 + charsCtr])
            i = hashIndex + 1 + charsCtr
        return res

