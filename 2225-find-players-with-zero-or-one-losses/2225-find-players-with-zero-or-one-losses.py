class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic = {} 
        winners = []
        losers = []
        for team in matches:
            if team[1] not in dic : 
                dic[team[1]] = 1
            else: 
                dic[team[1]] +=1    
            if team[0] not in dic : 
                dic[team[0]] = 0
           
            
        for team , value in dic.items():
            if value == 0 : 
                winners.append(team)
            if value == 1:
                losers.append(team)
        return [sorted(winners) , sorted(losers)]
            
                
                
            