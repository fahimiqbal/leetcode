class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        check = {}
        
        for n in nums:
            if check.get(n):
                return True
            check[n] = 1
            
        return False
        """
        
        check = set()
        
        for n in nums:
            if n in check: return True
            
            check.add(n)
            
        return False