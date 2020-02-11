class Solution:
    def reverse(self, a: int) -> int:
        neg = 0
        if a < 0:
            a = a - 2*a
            neg = 1

        b = list(str(a))
        b.reverse()
        c = "".join(b)
        d = int(c)
        if d > (2 ** 31 - 1) or d < (-2 ** 31):
            return 0

        if (neg == 1):
            d = d - 2*d
            return d
        else:
            return d