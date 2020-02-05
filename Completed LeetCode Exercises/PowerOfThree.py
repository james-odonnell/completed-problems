def isPowerOfThree(n):
    y = 0
    if n == 0:
        return False
    while y <= n:
        if (3 ** y) / n == 1:
            return True
        else:
            y = y + 1
            if (3 ** y) > n:
                return False



print(isPowerOfThree(27))
print(isPowerOfThree(9))
print(isPowerOfThree(0))
print(isPowerOfThree(45))