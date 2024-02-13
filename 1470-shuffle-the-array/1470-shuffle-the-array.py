class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return (nums[j] for i in range(n) for j in range(i, i + n + 1, n))
