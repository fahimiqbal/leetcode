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
        
        '''
        if len(nums) < 2:
            return False
        
        check = set()
        
        l = 0
        r = len(nums) - 1
        
        
        while l < r:
            if nums[l] == nums[r]:
                return True
            if nums[l] in check or nums[r] in check:
                return True
            
            check.add(nums[l])
            check.add(nums[r])
            
            l += 1
            r += -1
            
        if l==r:
            if nums[l] in check:
                return True
            
        return False
        '''
        
        check = set()
        
        for n in nums:
            if n in check: return True
            
            check.add(n)
            
        return False