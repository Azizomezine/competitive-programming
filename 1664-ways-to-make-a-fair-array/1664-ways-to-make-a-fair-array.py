class Solution:
    def waysToMakeFair(self, A):
        s1, s2 = [0, 0], [sum(A[0::2]), sum(A[1::2])]
        res = 0
        for i, a in enumerate(A):
            s2[i % 2] -= a
            res += s1[0] + s2[1] == s1[1] + s2[0]
            s1[i % 2] += a
        return res