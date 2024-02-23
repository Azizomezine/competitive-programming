class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reslt=[]
        
        for numb in range(len(nums)): 
            value=target-nums[numb]
            
            for j in range(len(nums)):
                    if nums[j]==(target-nums[numb]) and j != numb:
                        reslt.append(numb)
        return reslt
            
        