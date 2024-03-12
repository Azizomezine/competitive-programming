class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        m, n = len(M), len(M[0])
        ans = [[0] * n for _ in M]
        
        for i in range(m):
            i0, i1 = max(0, i-1), min(m, i+2)
            for j in range(n):
                j0, j1 = max(0, j-1), min(n,j+2)
                neighbors = [M[i_][j_] for i_ in range(i0, i1) for j_ in range(j0, j1)]
                ans[i][j] = int(sum(neighbors)/len(neighbors))
        return ans