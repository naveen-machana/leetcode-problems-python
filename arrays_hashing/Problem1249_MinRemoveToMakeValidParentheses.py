class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        temp = []
        cnt = 0
        for c in s:
            if c != '(' and c != ')':
                temp.append(c)
            elif c == ')' and cnt > 0:
                temp.append(c)
                cnt -= 1
            elif c == '(':
                temp.append(c)
                cnt += 1
        res = []
        for i in temp[::-1]:
            if temp[i] == '(' and cnt > 0:
                cnt -= 1
            else:
                res.append(temp[i])
        res = res[::-1]
        return "".join(res)




