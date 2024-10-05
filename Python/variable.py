# Variable declarations
counter = 100          # Integer variable
miles = 1000.0         # Floating point variable
name = "Zara Ali"      # String variable

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