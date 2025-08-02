class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left,right = 0,len(nums)-1
        
        while (right >= left):

            index = (left + right) // 2

            if (target == nums[index]):
                return index
            if (target > nums[index]):
                left = index + 1
            else:
                right = index - 1
        
        return left
        
        




            

        