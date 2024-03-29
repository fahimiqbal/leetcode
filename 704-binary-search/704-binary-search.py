class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = start + ((end - start) // 2)
            
            if nums[mid] > target:
                end -= 1
            elif nums[mid] < target:
                start += 1
            else:
                return mid
            
        return -1