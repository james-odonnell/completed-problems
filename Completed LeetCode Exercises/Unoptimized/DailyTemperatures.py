def dailyTemperatures(T):
    D = []
    for i in range(len(T)):
        count = 0
        for j in range(i + 1, len(T)):
            if (T[i] < T[j]):
                count = count + 1
                D.append(count)
                break
            elif (j == len(T)-1):
                count = 0
                D.append(count)
            else:
                count = count + 1
    # Since the last value of the array will never have a value higher than it, a 0 can be appended.
    D.append(0)
    return D


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))