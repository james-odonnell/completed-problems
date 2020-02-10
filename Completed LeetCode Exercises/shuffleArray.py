import random


class Solution:

    def __init__(self, nums):
        self.defaultarray = nums
        self.array = random.sample(nums,len(nums))


    def reset(self):
        return self.defaultarray


    def shuffle(self):
        random.shuffle(self.array)
        return self.array


num = [1,2,3]
solution = Solution(num)
print(solution.reset())
print(solution.shuffle())
print(solution.reset())



