class Solution(object):
    def isPathCrossing(self, path):
        points = set()
        points.add(tuple([0, 0]))
        cur = [0, 0]
        dir = {'N': [1, 0], 'E': [0, 1], 'S': [-1, 0], 'W': [0, -1]}
        for c in path:
            p = dir[c]
            cur[0] += p[0]
            cur[1] += p[1]
            next = tuple(cur)
            if next in points: return True
            points.add(next)
        return False
