class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarySearch(array,target,is_left):
            left,right = 0,len(nums)-1
            idx = -1
            while(right>=left):
                mid = (left+right)/2

                if (target < nums[mid]):
                  right = mid - 1 
                elif (target > nums[mid]):
                    left = mid + 1
                else:
                    idx = mid
                    if (is_left):
                        right = mid - 1
                    else:
                        left = mid + 1
                
            return idx
                
        left = binarySearch(nums,target,is_left=True)
        right = binarySearch(nums,target,is_left=False)

        return [left,right]

        
        