class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            cur = len([el for el in nums if el < nums[i]])
            res.append(cur)
        
        return res