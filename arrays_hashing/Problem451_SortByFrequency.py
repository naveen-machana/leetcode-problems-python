import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        buckets = collections.defaultdict(list) # freq -> list
        for c, n in counter.items():
            buckets[n].append(c)

        res = []
        for i in range(len(s), 0, -1):
            for c in buckets[i]:
                res.append(c * i)

        return "".join(res)