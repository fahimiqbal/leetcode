class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i, n in enumerate(nums):
            if i == 0:
                nums[count] = n
                count += 1
            else:
                if nums[i] != nums[i - 1]:
                    nums[count] = n
                    count += 1
                    
        return count