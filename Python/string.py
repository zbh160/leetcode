def split_and_join(line):
    # write your code here
    return "-".join(line.split(" "))
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

    fruits = ["apple", "banana", "cherry"]
    print(", ".join(fruits))  # Output: "apple, banana, cherry"

    s = "apple,banana,cherry"
    print(s.split(","))  # Output: ['apple', 'banana', 'cherry']

    s = "Hello"
    print(len(s))  # Output: 5

    s = "HELLO"
    print(s.lower())  # Output: "hello"

    s = "Hello World"
    print(s.swapcase())  # Output: "hELLO wORLD"

    s = "hello world"
    print(s.title())  # Output: "Hello World"

    s = "hello world"
    print(s.capitalize())  # Output: "Hello world"

    s = "   Hello   "
    print(s.strip())  # Output: "Hello"

    s = "   Hello   "
    print(s.lstrip())  # Output: "Hello   "
    print(s.rstrip())  # Output: "   Hello"

    s = "Hello World"
    print(s.replace("World", "Python"))  # Output: "Hello Python"

    s = "Hello World"
    print(s.startswith("Hello"))  # Output: True
    print(s.endswith("World"))  # Output: True

    s = "Hello World"
    print(s.find("World"))  # Output: 6

    s = "banana"
    print(s.count("a"))  # Output: 3

    s = "42"
    print(s.zfill(5))  # Output: "00042"

    s = "Hello"
    print(s.center(10))  # Output: "  Hello   "

    name = "Alice"
    age = 30
    print("My name is {} and I am {} years old".format(name, age))

    # Operator

    str1 = "Hello"
    str2 = "World"
    result = str1 + " " + str2  # "Hello World"

    repeated = "Ha" * 3  # "HaHaHa"

    str1 = "Hello"
    substring = "lo"
    result = substring in str1  # True

    # Example for string tricks
    text = "  Hello, World!   "
    # Reverse the string
    print("Reversed:", text[::-1])

    # Check for palindrome
    print("Is palindrome:", is_palindrome("racecar"))

    # Count vowels and consonants
    vowels, consonants = count_vowels_consonants(text)
    print(f"Vowels: {vowels}, Consonants: {consonants}")

    # Remove duplicates
    print("No duplicates:", remove_duplicates("banana"))

    # Formatting
    name = "Alice"
    age = 30
    print(f"My name is {name} and I am {age} years old.")

    # Join a list
    words = ["Hello", "World"]
    print("Joined:", " ".join(words))
