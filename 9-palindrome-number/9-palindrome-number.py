class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # below is the simplest solution converting in string and reverse
        #return str(x) == str(x)[::-1]
        
        # below is the solution without converting into string
        number = x
        reverse = 0 
        while(x > 0):    
            reminder = x % 10    
            reverse = (reverse * 10) + reminder    
            x = x // 10 
            
        return number == reverse
        