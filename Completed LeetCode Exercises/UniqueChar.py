def firstUniqChar(s):
    f = []
    for i in set(s):
        if s.count(i) == 1:  # check to see if the character is unique
            f.append(s.index(i))  # adds the index of the unique character to the array
    if len(f) > 0:
        return min(f)  # returns the first instance of a unique character
    else:
        return -1  # if it isn't found, returns -1


print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
