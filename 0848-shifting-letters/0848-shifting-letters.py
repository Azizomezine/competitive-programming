class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        sumArr=[shifts[len(s)-1]%26]
        new=""
        for i in range(1,len(s)):
            sumArr.insert(0,(sumArr[0]+shifts[len(s)-i-1])%26)
        for i in range(len(s)):
            n=ord(s[i])+sumArr[i]
            if n>ord("z"):
                n-=26
            new+=chr(n)
        return new