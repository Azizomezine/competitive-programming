class Solution:
	def dividePlayers(self, skill: List[int]) -> int:

		skill = sorted(skill)

		result = 0
		length = len(skill)

		equal_sum = skill[0] + skill[-1]
		result = result + skill[0] * skill[-1]

		for index in range(1, length//2):

			current_sum = skill[index] + skill[length - index - 1]

			if current_sum == equal_sum:
				result = result + skill[index] * skill[length - index - 1]
			else:
				return -1

		return result