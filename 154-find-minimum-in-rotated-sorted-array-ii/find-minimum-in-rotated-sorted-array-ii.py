class Solution(object):
            
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        start = 0
        end = 0
        
        if len(nums) == 1:
            return nums[0]
        while (start <= end and end != len(nums)-1):
            end += 1
            
            if nums[start] > nums[end]:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
            
            
                
        return nums[0]
                