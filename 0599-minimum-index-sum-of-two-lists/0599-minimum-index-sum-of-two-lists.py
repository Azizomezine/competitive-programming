class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    	D = {j:i for i,j in enumerate(list2)}
    	L = sorted([[i+D[j],j] for i,j in enumerate(list1) if j in D])
    	return [r[1] for r in L if r[0] == L[0][0]]