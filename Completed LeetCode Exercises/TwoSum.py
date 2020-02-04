from typing import List

# My Solution (passes all but one test case- runs too slowly in test cases with lots of list elements)

class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(len(nums)):
                if nums[x] + nums[y] == target:
                    if x != y:
                     return[x,y]
                    else:
                        continue

a = Solution.twoSum([2,5,5,15], 10)
print(a)


