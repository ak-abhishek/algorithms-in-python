def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


def factorial2(number):
    return reduce(lambda x, y: x * y, [i for i in range(1, number + 1), 1])
