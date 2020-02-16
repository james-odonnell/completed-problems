def swap_case(s):
    d = ""
    for ele in s:
        if ele.islower():
            d = d + ele.capitalize()

        else:
            d = d + ele.lower()

    return d


print(swap_case("Hello World"))







