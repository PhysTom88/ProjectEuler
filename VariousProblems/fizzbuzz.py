from __future__ import print_function


def fizzbuzz(number):
    if (number % 3 == 0 and number % 5 == 0):
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)


for i in range(1, 100):
    print(fizzbuzz(i))
