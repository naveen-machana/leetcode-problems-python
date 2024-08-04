class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        l = 0
        for r in range(len(s)):
            if s[r] == ' ' or r == len(s) - 1:
                templ, tempr = l, r - 1
                if r == len(s) - 1: tempr = r

                while templ < tempr:
                    s[templ], s[tempr] = s[tempr], s[templ]
                    templ, tempr = templ + 1, tempr - 1
                l = r + 1

        return ''.join(s)