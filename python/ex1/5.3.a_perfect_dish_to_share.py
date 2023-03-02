# מנה מושלמת לחלוקה
import math


def is_perfect_num(num):
    _sqrt = math.sqrt(num)

    sum_dividers = 0

    for i in range(2, math.ceil(_sqrt)):
        if num % i == 0:
            sum_dividers = sum_dividers + i + num / i

    if _sqrt == int(_sqrt):
        sum_dividers = sum_dividers + _sqrt

    return sum_dividers + 1 == num


def perfect_number_generator():
    num = 1

    while True:
        if is_perfect_num(num):
            yield num
        num = num + 1

gen =perfect_number_generator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))