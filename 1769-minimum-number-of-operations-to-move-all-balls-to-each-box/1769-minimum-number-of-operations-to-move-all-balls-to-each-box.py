class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ones = [i for i in range(0 , len(boxes)) if boxes[i] == '1']
        
        ans = []
        
        for i in range(0 , len(boxes)):
            tot = 0
            for j in ones:
                tot += abs(j - i)
            ans.append(tot)
        
        return ans