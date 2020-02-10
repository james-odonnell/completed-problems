# Given an array nums of integers, return how many of them contain an even number of digits.

def findNumbers(nums):
    counter = 0
    for ele in nums:
        if len(str(ele)) % 2 == 0:
            counter = counter + 1
    return counter


print(findNumbers([1, 234, 56, 7890]))