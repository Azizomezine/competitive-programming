class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        
        leftPointer = len(nums) - 1
        
        while leftPointer > 0 and nums[leftPointer - 1] >= nums[leftPointer]:
            leftPointer -= 1
            
        
        if leftPointer > 0:
            start = leftPointer
            end = len(nums) - 1
     
            while start <= end:
                mid = (start + end) // 2

                if nums[mid] <= nums[leftPointer - 1]:
                    end = mid - 1
                else:
                    start = mid + 1
                


            nums[end], nums[leftPointer - 1] = nums[leftPointer - 1], nums[end]
        
        rightPointer = len(nums) - 1
        
        while leftPointer < rightPointer:
            nums[leftPointer], nums[rightPointer] = nums[rightPointer], nums[leftPointer]
            leftPointer += 1
            rightPointer -= 1