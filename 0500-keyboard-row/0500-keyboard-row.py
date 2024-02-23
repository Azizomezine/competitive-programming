
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ligne1="qwertyuiop"
        ligne2="asdfghjkl"
        ligne3="zxcvbnm"
        i=0
        reslt=[]
        for j in words:
            word= set(j.lower())
            if word.issubset(ligne1) or word.issubset(ligne2) or word.issubset(ligne3):
                reslt.append(j)
        return reslt
    
             


                
                        
        