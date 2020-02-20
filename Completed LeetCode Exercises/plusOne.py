class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = []
        for ele in reversed(digits):
            d.append(ele)
        d[0] = d[0] + 1

        if len(d) < 2:
            if d[0] == 10:
                d.append(1)
                d[0] = 0

        for ele in range(len(d) - 1):
            if d[ele] > 9:
                d[ele] = 0
                d[ele + 1] = d[ele + 1] + 1
                if d[-1] == 10:
                    d[-1] = 0
                    d.append(1)
        d.reverse()

        return d

