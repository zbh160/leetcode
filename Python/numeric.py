def split_and_join(line):
    # write your code here
    return
def print_full_name(first, last):
    # Write your code here
    print("Hello {} {}! You just delved into python.".format(first, last))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

    # Basic
    a = 10
    b = 3
    print(a + b)  # 13
    print(a - b)  # 7
    print(a * b)  # 30
    print(a / b)  # 3.3333...
    print(a // b)  # 3
    print(a % b)  # 1
    print(a ** b)  # 1000

    # abs
    print(abs(-10))  # 10

    # round
    print(round(3.14159, 2))  # 3.14

    # max and min
    print(max([1, 2, 3, 4, 5]))  # 5
    print(min([1, 2, 3, 4, 5]))  # 1

    # sum
    print(sum([1, 2, 3, 4, 5]))  # 15

    # power
    print(pow(2, 3))  # 8
    print(pow(2, 3, 3))  # 2

    # sqrt
    import math

    print(math.sqrt(16))  # 4.0

    # factorial
    print(math.factorial(5))  # 120

    # ceil and floor
    print(math.ceil(4.2))  # 5
    print(math.floor(4.7))  # 4

    import math
    import random

    # Arithmetic
    a = 10
    b = 3
    print("Sum:", a + b)
    print("Product:", a * b)

    # Using functions
    print("Absolute:", abs(-7))
    print("Max:", max(a, b))
    print("Sum:", sum([1, 2, 3, 4, 5]))

    # Square root and factorial
    print("Square root:", math.sqrt(25))
    print("Factorial of 5:", math.factorial(5))

    # Random number
    random_num = random.randint(1, 100)
    print("Random number:", random_num)

    # List comprehension
    squares = [x ** 2 for x in range(10)]
    print("Squares:", squares)
    # Example for numeric tricks
    import math
    import random

    # Arithmetic
    a = 10
    b = 3
    print("Sum:", a + b)
    print("Product:", a * b)

    # Using functions
    print("Absolute:", abs(-7))
    print("Max:", max(a, b))
    print("Sum:", sum([1, 2, 3, 4, 5]))

    # Square root and factorial
    print("Square root:", math.sqrt(25))
    print("Factorial of 5:", math.factorial(5))

    # Random number
    random_num = random.randint(1, 100)
    print("Random number:", random_num)

    # List comprehension
    squares = [x ** 2 for x in range(10)]
    print("Squares:", squares)