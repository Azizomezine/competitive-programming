class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        v = 'aeiou'
        num = []
        l = 0 
        for w in words:
            if w[0] in v and w[-1] in v:
                l += 1
                num.append(l)
            else:
                num.append(l)
        res = []
        for a, b in queries:
            if a != 0:
                res.append(num[b] - num[a-1])
            else:
                res.append(num[b])
        
        return res