class Solution:
	def isPowerOfThree(self, n: int) -> bool:
		if (n == 0):
			return False
		def recursion(n):
			if (n == 1):
				return True
			if (n%3 != 0):
				return False
			return recursion(n/3)

		return recursion(n)