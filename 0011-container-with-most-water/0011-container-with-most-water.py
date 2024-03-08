class Solution:
    def maxArea(self, height: List[int]) -> int:
        # we need to store the maximum area to compare it 
        Max = 0
        i = 0 
        j = len(height)-1
        while i < j : 
            # width 
            widh = j - i 
            if height[j] > height[i]:
                Maxh = height[i]
                i+=1

            else:
                Maxh = height[j]
                j-=1
            area = widh * Maxh
            if area > Max :
                Max = area
        return Max
                
         