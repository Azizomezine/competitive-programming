#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        #code here
        set_a= set(a)
        set_b= set(b)
        return len(set(a) | set(b))

