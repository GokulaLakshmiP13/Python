# Function to check if a number is even (returns a boolean value)
def is_even_with_return(n):
    """
    :param n: Positive integer
    :return: True if n is even, else False
    """
    return n % 2 == 0

# Function to check if a number is even (prints result instead of returning)
def is_even_without_return(n):
    """
    :param n: Positive integer
    :return: None (just prints)
    """
    print(f"{n} is even? {n % 2 == 0}")

# Function to add two numbers and return result
def add(x, y):
    return x + y  # Can be used in further calculations

# Function to multiply two numbers and print result (does not return)
def mult(x, y):
    print(x * y)  # Just prints result

# Function to check if a number is triangular
def is_triangular(n):
    """
    Checks whether n is triangular
    :param n: Positive integer
    :return: True if n is triangular, else False
    """
    total = 0
    for i in range(n):
        total += i
        if total == n:
            return True
    return False

# Function to find square root using Bisection Search
def bisection_search_square_root(x):
    """
    Evaluates square root using the bisection search method
    :param x: Positive integer
    :return: Approximate square root of x
    """
    epsilon = 0.01  # Precision limit
    if x >= 1:
        low, high = 1, x
    else:
        low, high = x, 1

    guess = (low + high) / 2
    while abs(guess ** 2 - x) >= epsilon:
        if guess ** 2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
    return guess

# Function to count numbers whose square root is close to n
def count(n, epsilon):
    """
    Count how many integers have a square root within a range
    :param n: Positive integer greater than 2
    :param epsilon: Small positive number
    :return: Count of integers that satisfy condition
    """
    countsquares = 0
    for i in range(n**3):
        sqrt = bisection_search_square_root(i)
        if abs(n - sqrt) < epsilon:
            print(i, sqrt)
            countsquares += 1
    return countsquares

# Function that takes another function as a parameter
def calc(op, x, y):
    """
    Performs an operation on x and y
    :param op: Function to be applied
    :param x: First number
    :param y: Second number
    :return: Result of applying op to x and y
    """
    return op(x, y)

# Function to divide two numbers safely
def div(x, y):
    """
    Safe division function
    :param x: Numerator
    :param y: Denominator
    :return: x/y if y != 0, else prints an error
    """
    if y != 0:
        return x / y
    print("Denominator cannot be 0")

# Function returning another function's result
def func_a():
    print("Inside func_a")

def func_b(y):
    print("Inside func_b")
    return y

def func_c(f, z):
    print("Inside func_c")
    return f(z)

# Function to count numbers that meet a given criteria
def apply(criteria, n):
    """
    Counts how many numbers satisfy the given criteria
    :param criteria: Function that checks a condition
    :param n: Upper bound (inclusive)
    :return: Count of numbers satisfying criteria
    """
    count = 0
    for i in range(n + 1):
        if criteria(i):
            count += 1
    return count

# MAIN PROGRAM EXECUTION
print(f"6 is even? {is_even_with_return(6)}")
print(f"87 is even? {is_even_with_return(87)}")

print("Without return:")
is_even_without_return(9)
is_even_without_return(62)
is_even_without_return(52)  # Proper way to call function without return value

# Demonstration of functions with and without return
print(add(2, 3))  # Returns 5
mult(3, 4)  # Prints 12
print(mult(4, 5))  # Prints 20, then None

# Checking triangular numbers
print(f"Is 6 triangular? {is_triangular(6)}")
print(f"Is 5 triangular? {is_triangular(5)}")

# Finding square root using Bisection Search
print(f"Square root of 6 is close to {bisection_search_square_root(6)}")

# Counting numbers based on square root condition
print(count(15, 0.1))

# Function usage with higher-order functions
print(calc(add, 6, 8))  # 14
print(calc(mult, 6, 8)) # 48
print(calc(div, 6, 8))  # 0.75

res = calc(div, 2, 0)  # Prints error and returns None
print(res)

# Function calls demonstration
print(func_a())  # Prints "Inside func_a" and returns None
print(5 + func_b(2))  # Prints "Inside func_b" and returns 7
print(func_c(func_b, 3))  # Calls func_b inside func_c

# Applying a condition function (is_even) to a range of numbers
print(apply(is_even_with_return, 8))  # Counts even numbers from 0 to 8
