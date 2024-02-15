class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        bl=[]
        
        for candy in candies : 
            
            ex=candy+extraCandies
            if ex >= max(candies) :
                bl.append(True)
            else : 
                bl.append(False)
        return  bl
                
        
            
            
        
  