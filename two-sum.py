class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        checked = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
           
            if remaining in checked:
                return [checked[remaining], i]
            
            checked[value] = i 
