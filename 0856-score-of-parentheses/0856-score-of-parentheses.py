class Solution:
    def scoreOfParentheses(self, s: str) -> int:
            x = []
            for i in s:
                if i=='(':
                    x.append(i)
                else:
                    n= 0
                    while x and x[-1]!='(':
                        n+=x.pop()
                    x.pop()
                    if n!=0:
                        x.append(2*n)
                    else:
                        x.append(1)
            return sum(x)    