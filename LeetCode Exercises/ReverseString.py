def reverseString(s):
    a = 0
    b = len(s) - 1
    while a < b:
        s[a], s[b] = s[b], s[a]
        a = a + 1
        b = b - 1
