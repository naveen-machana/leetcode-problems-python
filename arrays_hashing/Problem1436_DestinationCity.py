class Solution(object):
    def destCity(self, paths):
        starts = set()
        for path in paths:
            starts.add(path[0])
        for path in paths:
            if path[1] not in starts:
                return path[1]
        return ''