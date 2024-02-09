class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dic= {}
        if len(nums) == 0 :
            return 1
        else:
            for number in range(0,len(nums)+1):
                if number in nums : 
                    dic[number]= 1
                else:
                    dic[number] = 0
            for number,value in dic.items():
                if value == 0 : 
                    return number