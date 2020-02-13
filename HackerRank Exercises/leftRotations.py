# a is the length of the array, b is the number of rotations

def rotateLeft(a,b):
    rotations = 0
    temp = 0
    l = len(a)
    while rotations < b:
        temp = a[0]
        a.pop(0)
        a.append(temp)
        rotations = rotations + 1
    return a


print(rotateLeft([1,2,3,4,5],1))


