def subtractProductAndSum(n):
    numlist = []
    totalSum = 0
    product = 1
    for x in str(n):
        numlist.append(x)

    for y in numlist:
        totalSum = int(y) + totalSum
        product = int(y) * product

    return (product - totalSum)



print(subtractProductAndSum(234))
print(subtractProductAndSum(4421))


