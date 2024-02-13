class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num = {n: i for i, n in enumerate(nums)}
        for n1, n2 in operations:            
            num[n2] = num.pop(n1)
            
        result = [0] * len(nums)
        for n, i in num.items():
            result[i] = n
        
        return result