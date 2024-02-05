class Solution:
    def defangIPaddr(self, address: str) -> str:
        st=""
        for i in address:
            if i == ".":
                st+='['+'.'+']'
            else:
                st+=i   
        return st      