# Variable declarations
counter = 100          # Integer variable
miles = 1000.0         # Floating point variable
name = "Zara Ali"      # String variable

# Bad:
x = 10

# Good:
item_count = 10

total_price = 100.50
user_name = "John"

# Okay in loops:
for i in range(10):
    print(i)

# Avoid elsewhere:
x = 5  # Too vague, use a more descriptive name.

# Bad:
list = [1, 2, 3]  # `list` is a built-in function.

# Good:
numbers_list = [1, 2, 3]

# Bad:
price_of_the_item_in_the_cart = 50.00  # Too long.

# Good:
item_price = 50.00  # Concise yet descriptive.

_private_variable = 42

PI = 3.14159
MAX_CONNECTIONS = 100

# Bad:
2nd_value = 100

# Good:
second_value = 100

# Print

name = "Alice"
age = 30
print("Name:", name, "Age:", age)

name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

print("My name is {} and I am {} years old.".format(name, age))

print("Hello", end=" ")
print("World!")
# Output: Hello World!

print("apple", "banana", "cherry", sep=", ")
# Output: apple, banana, cherry

with open("output.txt", "w") as f:
    print("Writing to file", file=f)

age = 30
print(f"Age: {age}, Type: {type(age)}")
print("Line 1\nLine 2")
print("Tab\tSeparated")

raw_data = "Hello\nWorld"
print(repr(raw_data))  # Output: 'Hello\nWorld'

x = 5
print(f"x is {'even' if x % 2 == 0 else 'odd'}")

import sys

print("Visible output")
sys.stdout = None  # Suppress further print output
print("This will not be printed")
sys.stdout = sys.__stdout__  # Restore print functionality


# Deleting variables
del miles, name

# Checking the type of 'counter'
print(type(counter))

# Type conversion
x = str(10)    # x will be '10'
y = int(10)    # y will be 10
z = float(10)  # z will be 10.0

# Multiple assignment
a, b, c = 1, 2, "Zara Ali"

# Function with local variables
def sum_local(x, y):
    return x + y

print(sum_local(5, 10))

# Global variables example
x = 5
y = 10

def sum_global():
    return x + y

print(sum_global())