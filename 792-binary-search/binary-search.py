class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low,height = 0,len(nums)-1

        while (low <= height):

            mid = (low+height)//2

            if (nums[mid] == target):
                return mid
            
            if (target > nums[mid]):
                low = mid + 1
            else:
                height = mid - 1
        return -1
            
        



