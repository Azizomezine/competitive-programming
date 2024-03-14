class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        i, n = 0, len(nums)-1
        forward, backward = [0]*(n+2), [0]*(n+2)
        while i <= n:
            if nums[i] == 0: forward[i+1] = forward[i] + 1
            else: forward[i+1] = forward[i]
            if nums[n-i] == 1: backward[n-i] = backward[n-i+1] + 1
            else: backward[n-i] = backward[n-i+1]
            i += 1
        ans, prev = [], 0
        for i in range(n+2):
            total = forward[i] + backward[i]
            if total > prev:
                prev = total
                ans = [i]
            elif total == prev: ans.append(i)
        return ans