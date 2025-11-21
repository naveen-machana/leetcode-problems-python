class Solution(object):
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            visited[i][j] = True

            for x, y in directions:
                nxtx, nxty = i + x, j + y
                if 0 <= nxtx < m and 0 <= nxty < n and not visited[nxtx][nxty] and grid[nxtx][nxty] == 1:
                    print(nxtx, nxty)
                    dfs(nxtx, nxty)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    dfs(i, j)
                    res += 1

        return res
