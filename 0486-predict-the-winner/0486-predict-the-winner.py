class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) <= 2 : 
            return True

        def rec(left , right) :
            if left == right :
                return nums[left]

            if_chosen_left = nums[left] - rec(left + 1 , right)
            if_chosen_right = nums[right] - rec(left , right - 1)

            return max(if_chosen_left , if_chosen_right)

        return rec(0 , len(nums)-1) >= 0