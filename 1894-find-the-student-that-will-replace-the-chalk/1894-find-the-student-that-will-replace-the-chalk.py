class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sums = sum(chalk)
        div = k // sums
        k = k - (sums * div)
        for i in range(len(chalk)):
            if chalk[i] <= k:
                k -= chalk[i]
            else:
                return i
        return -1