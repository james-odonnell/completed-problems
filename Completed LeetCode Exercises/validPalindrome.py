import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = re.split(r'\W+', s)
        y = ''
        for ele in x:
            y = y + ele

        z = y[::-1]

        return y.lower() == z.lower()
