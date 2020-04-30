def same_necklace(necklace1, necklace2):
    if necklace1 == necklace2:
        return True
    x = []
    c = necklace1
    necklace_length = len(necklace1) - 1
    a = 0
    while a < necklace_length:
        c = (c[1:] + c[0:1])
        x.append(c)
        a += 1

    return necklace2 in x


print(same_necklace("nicole", "icolen")) #=> true
print(same_necklace("nicole", "lenico")) #=> true
print(same_necklace("nicole", "coneli")) #=> false
print(same_necklace("aabaaaaabaab", "aabaabaabaaa")) #=> true
print(same_necklace("abc", "cba")) #=> false
print(same_necklace("xxyyy", "xxxyy")) #=> false
print(same_necklace("xyxxz", "xxyxz")) #=> false
print(same_necklace("x", "x")) #=> true
print(same_necklace("x", "xx")) #=> false
print(same_necklace("x", "")) #=> false
print(same_necklace("", "")) #=> true