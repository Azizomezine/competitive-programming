class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        N = len(heights)
        for i in range(N-1):
            for j in range(N-i-1):
                if heights[j] > heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
        return names[::-1]
                
                
                
            
        