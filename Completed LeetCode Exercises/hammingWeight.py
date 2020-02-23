class Solution:
    def hammingWeight(self, n: int) -> int:
        a = bin(n)
        count = 0
        b = list(str(a))
        for ele in b:
            if ele == '1':
                count = count + 1
        return count
