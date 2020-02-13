import sys

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    count = 0
    n = len(a)
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                count = count + 1


    print("Array is sorted in " + str(count) + " swaps.\nFirst Element: " + str(a[0]) + "\nLast Element: " + str(a[-1]))

