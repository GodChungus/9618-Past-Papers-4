def IterativeCalculate(number):
    total, to_find = 0, number
    while number != 0:
        if to_find % number == 0:
            total += number
        number -= 1
    return total


def RecursiveValue(number, to_find):
    if number == 0:
        return 0
    else:
        if to_find % number == 0:
            return number + RecursiveValue(number-1, to_find)
        else:
            return RecursiveValue(number-1, to_find)


print(IterativeCalculate(10))
print(RecursiveValue(50, 50))