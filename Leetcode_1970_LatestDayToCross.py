import collections
class Solution(object):
    def create(self, row, col, cells):
        days = ['0'] * (row * col)
        daysStr = []
        daysStr.append(''.join(days))
        for x, y in cells:
            index = (x - 1) * col + (y - 1)
            days[index] = '1'
            daysStr.append(''.join(days))
        return daysStr

    def bfs(self, index, days, row, col):
        directions = [(0, -1), (0, 1), (1, 0)]
        daysMat = days[index]
        visited = [False] * len(daysMat)
        q = collections.deque()
        for i in range(col):
            if not visited[i] and daysMat[i] == '0':
                q.append((0, i))
                visited[i] = True

        while q:
            x, y = q.popleft()
            pos = x * col + y
            if daysMat[pos] == '1': continue
            if x == row - 1: return True
            for i, j in directions:
                nextx, nexty = x + i, y + j
                nextIndex = nextx * col + nexty
                if 0 <= nextx < row and 0 <= nexty < col and daysMat[nextIndex] != '1' and not visited[nextIndex]:
                    visited[nextIndex] = True
                    q.append((nextx, nexty))
        return False

    def latestDayToCross(self, row, col, cells):
        days = self.create(row, col, cells)
        print(days)
        l, r = 0, len(days)
        res = 0
        while l <= r:
            m = l + (r - l) // 2
            if self.bfs(m, days, row, col):
                res = m
                l = m + 1
            else:
                r = m - 1
        return res

sol = Solution()
cells = [[1,1],[2,1],[1,2],[2,2]]
res = sol.latestDayToCross(2,2,cells)
print(res)