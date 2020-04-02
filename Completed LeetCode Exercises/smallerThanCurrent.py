class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted = nums.copy()
        nums_sorted.sort()
        z = []
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums_sorted)):
                if nums[i] != nums_sorted[j]:
                    count += 1
                else:
                    z.append(count)
                    count = 0
                    break
        return z
