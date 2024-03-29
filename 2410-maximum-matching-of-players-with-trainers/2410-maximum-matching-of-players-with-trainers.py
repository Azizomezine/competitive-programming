class Solution:
    def matchPlayersAndTrainers(self, p: List[int], t: List[int]) -> int:
        p.sort()
        t.sort()
        i = j = res = 0
        while i < len(p) and j < len(t):
            if p[i] <= t[j]:
                res += 1
                i += 1
            j += 1
        return res