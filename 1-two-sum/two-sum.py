class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {} #val,index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[n] = i
        return