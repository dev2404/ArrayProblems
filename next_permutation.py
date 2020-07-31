#NEXT PERMUTATION PROBLEM
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        point = len(nums) - 2
        
        while point >= 0 and nums[point] >= nums[point+1]:
            point -= 1
            
        if point < 0:
            return []
       
        for i in reversed(range(point, len(nums))):
            if nums[i] > nums[point]:
                nums[i], nums[point] = nums[point], nums[i]
                break
        nums[point+1:] = reversed(nums[point+1:])
        return nums
