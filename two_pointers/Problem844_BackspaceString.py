class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def nextValidChar(str, index):
            back = 0
            while index >= 0:
                if back == 0 and str[index] != '#':
                    return index
                elif str[index] == '#':
                    back += 1
                else:
                    back -= 1
                index -= 1
            return index

        indexS, indexT = len(s) - 1, len(t) - 1
        while indexS >= 0 or indexT >= 0:
            indexS = nextValidChar(s, indexS)
            indexT = nextValidChar(t, indexT)

            charS = s[indexS] if indexS >= 0 else ''
            charT = t[indexT] if indexT >= 0 else ''

            if charS != charT: return False
            indexS, indexT = indexS - 1, indexT - 1

        return True