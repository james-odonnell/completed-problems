#class Solution:
#    def missingNumber(self, nums: List[int]) -> int:
#        for ele in range(len(nums)+1):
#            if ele not in nums:
#                return ele

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        for x in range(len(nums)+1):
            s = s + x
        return s - sum(nums)