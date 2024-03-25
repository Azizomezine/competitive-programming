class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        maxLength = 0
        
        i,j = 0,1
        
        distincts = 0
        
        while j < len(word):
            if word[i] == "a":
                distincts = 1
                while j < len(word) and ord(word[j-1]) <= ord(word[j]):
                   
                    if ord(word[j-1]) < ord(word[j]): distincts += 1
                    j += 1
               
                if distincts == 5: maxLength = max(maxLength, j - i)                    
            
          
            i = j
            j += 1
            
        return maxLength
        