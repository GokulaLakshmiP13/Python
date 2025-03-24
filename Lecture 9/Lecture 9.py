def apply(criteria, n):
    """
    Counts how many numbers from 0 to n (inclusive) satisfy the given condition.
    :param criteria: A function that defines the condition.
    :param n: The upper bound (inclusive), where n > 0.
    :return: The count of numbers that meet the criteria.
    """
    count = 0
    for i in range(n + 1):
        if criteria(i):
            count += 1
    return count

# Using a lambda function to count even numbers in the range 0 to 10
print("Count of even numbers from 0 to 10:", apply(lambda x: x % 2 == 0, 10))

# Output of the following function
def do_twice(n, fn):
    """
    Applies the given function twice on the input number.
    :param n: An integer input.
    :param fn: A function to be applied twice.
    :return: The result after applying the function twice.
    """
    return fn(fn(n))

print(do_twice(3, lambda x: x ** 2))  # Output: 81

# Working with tuples
tuple_ex = (1, "Hello", 6.5, (5, 6))
print("Length of the tuple:", len(tuple_ex))
print("Tuple contents:", tuple_ex)

# Iterating over tuple elements
for ex in tuple_ex:
    print(ex)

# Using a tuple to return multiple values from a function
def division(x, y):
    """
    Performs division and returns both quotient and remainder.
    :param x: A positive integer (dividend).
    :param y: A positive integer (divisor).
    :return: A tuple containing (quotient, remainder).
    """
    q = x // y
    r = x % y
    return (q, r)

(quotient, remainder) = division(10, 3)

print(f"Quotient = {quotient}, Remainder = {remainder}")

def char_count(s):
    """
    Determines the number of vowels and consonants in the given string.
    :param s: A string containing only lowercase letters.
    :return: A tuple - first value is vowel count, second value is consonant count.
    """
    (v, c) = (0, 0)
    for i in s:
        if i in "aeiou":
            v += 1
        else:
            c += 1
    return (v, c)

print(char_count("hello"))

# Function to add multiple numbers using variable-length arguments
def add(*args):
    """
    Computes the sum of all given numbers.
    :param args: A variable number of numeric arguments.
    :return: The sum of all provided numbers.
    """
    total = 0
    for i in args:
        total += i
    return total

print(add(4, 8, 6, 0, 5, 7))
print(add(7, 0, 4))

# Function to sum elements of a list
def list_sum(L):
    """
    Computes the sum of all numbers in a given list.
    :param L: A list of numeric values.
    :return: The sum of all elements in the list.
    """
    total = 0
    for i in L:
        total += i
    return total

print(list_sum([1, 9, 6, 8]))

# Function to compute both sum and product of a list
def sum_product(L):
    """
    Calculates both the sum and the product of elements in a list.
    :param L: A list of numbers.
    :return: A tuple - first value is sum, second value is product of all elements.
    """
    (total_sum, total_product) = (0, 1)

    for i in L:
        total_sum += i
        total_product *= i

    return (total_sum, total_product)

ans = sum_product([6, 9, 4, 2, 1])

print(f"Sum = {ans[0]}, Product = {ans[1]}")
