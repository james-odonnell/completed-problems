def numJewelsInStones(J, S):
    count = 0
    for ele in J:
        for ele2 in S:
            if ele == ele2:
                count = count + 1
    return count

print(numJewelsInStones("aA", "aAAbbbb"))