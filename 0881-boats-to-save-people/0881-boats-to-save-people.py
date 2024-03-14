class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        boat = 0
        l  = 0 
        r = len(people) - 1
     
        people.sort()
        while l <= r:
            if people[r] + people[l] <= limit:
                l += 1
            r -= 1
            boat += 1
        return boat