# Function to check if a number is even
def is_even(n):
    """
    :param n: n is a positive integer
    :return: Bool True if n is even, False if n is odd
    """
    return n % 2 == 0  # Returns True if the remainder is 0 when divided by 2

# Testing the is_even function
print(is_even(5))  # False, since 5 is odd
print(is_even(62)) # True, since 62 is even


# Function to check if a number is divisible by another number
def div_by(n, d):
    """
    :param n: n is a positive integer
    :param d: d is another positive integer
    :return: Bool, True if d divides n, else return False
    """
    return n % d == 0  # Returns True if there is no remainder

# Testing the div_by function
print(div_by(51, 3))  # True, since 51 is divisible by 3
print(div_by(6, 4))   # False, since 6 is not divisible by 4


# Loop to check whether numbers from 1 to 9 are even or odd
for i in range(1, 10):  
    if is_even(i):  # Calls the is_even function
        print(i, "Even")  # Prints if the number is even
    else:
        print(i, "Odd")   # Prints if the number is odd


# Function to find the sum of all odd numbers between two given limits
def sum_odd(a, b):
    """
    :param a: Lower limit for starting to sum the odd numbers
    :param b: Upper limit for ending to sum the odd numbers
    :return: Sum of odd numbers between a and b
    """
    ans = 0  # Initialize sum variable
    for j in range(a, b + 1):  # Loop through numbers from a to b (inclusive)
        if not is_even(j):  # If the number is odd (i.e., is_even(j) returns False)
            ans += j  # Add the odd number to the sum
    return ans  # Return the total sum of odd numbers

# Testing the sum_odd function
print(sum_odd(1, 9))  # Output: 25 (1 + 3 + 5 + 7 + 9)
