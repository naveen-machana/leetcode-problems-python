from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        tCtr = Counter(t)
        sCtr = Counter()
        tlen = len(t)
        i, res, resStr, matchCtr = 0, float('inf'), '', 0
        for j in range(len(s)):
            sCtr[s[j]] += 1
            if s[j] in t and sCtr[s[j]] <= tCtr[s[j]]: matchCtr += 1
            while matchCtr == tlen and i <= j:
                if (j - i + 1) < res:
                    res = min(res, j - i + 1)
                    resStr = s[i: j + 1]
                sCtr[s[i]] -= 1
                if s[i] in t and sCtr[s[i]] < tCtr[s[i]]:
                    matchCtr -= 1
                i += 1
        return resStr

sol = Solution()
s, t = "ADOBECODEBANC", "ABC"
print(sol.minWindow(s, t))
