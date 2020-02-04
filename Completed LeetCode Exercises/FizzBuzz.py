def fizzbuzz(n):
    fb = []
    elem = 1
    while elem <= n:
        if elem % 3 == 0 and elem % 5 != 0:
            fb.append("Fizz")
            elem = elem + 1
        elif elem % 5 == 0 and elem % 3 != 0:
            fb.append("Buzz")
            elem = elem + 1
        elif elem % 5 == 0 and elem % 3 == 0:
            fb.append("FizzBuzz")
            elem = elem + 1
        else:
            fb.append(str(elem))
            elem = elem + 1
    return fb

print(fizzbuzz(15))