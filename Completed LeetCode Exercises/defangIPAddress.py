class Solution:
    def defangIPaddr(self, address: str) -> str:
        a = address.split('.')
        b = "[.]"
        b = b.join(a)
        return b
