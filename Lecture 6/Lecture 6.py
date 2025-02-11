# Finding the square root of a number using bisection search
x = 54321  # Number to find the square root of
epsilon = 0.01  # Precision level
n = 0  # Counter for number of guesses

low = 0  # Lower bound of search range
high = max(1, x)  # Ensures proper range for small x values
guess = (low + high) / 2  # Initial guess (midpoint)

while abs(guess**2 - x) >= epsilon and n < 1000:  # Prevent infinite loops
    if guess**2 < x:
        low = guess  # Move the lower bound up
    else:
        high = guess  # Move the upper bound down
    guess = (low + high) / 2  # Update guess to midpoint
    n += 1  # Increment guess counter

print(f"No. of guesses: {n}")
print(f"Square root of {x} is close to {guess:.5f}\n")

# Optimized program to handle values between 0 and 1
x = 0.5  # Small number to find the square root of
epsilon = 0.01
n = 0

if x < 0:
    print("Cannot compute the square root of a negative number.\n")
elif x == 0:
    print("Square root of 0 is 0.\n")
else:
    low, high = (x, 1) if x < 1 else (1, x)  # Adjust bounds
    guess = (low + high) / 2

    while abs(guess**2 - x) >= epsilon and n < 1000:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
        n += 1

    print(f"No. of guesses: {n}")
    print(f"Square root of {x} is close to {guess:.5f}\n")

# Bisection search algorithm to find the cube root of a number
cube = -27  # Test with negative values
epsilon = 0.01
n = 0

# Handle negative numbers correctly
if cube < 0:
    is_negative = True
    cube = -cube  # Work with the absolute value
else:
    is_negative = False

low, high = (cube, 1) if cube < 1 else (1, cube)
guess = (high + low) / 2

while abs(guess**3 - cube) >= epsilon and n < 1000:
    if guess**3 > cube:
        high = guess
    else:
        low = guess
    guess = (high + low) / 2
    n += 1

guess = -guess if is_negative else guess  # Restore negative sign if needed
print(f"No. of guesses: {n}")
print(f"Cube root of {cube if not is_negative else -cube} is close to {guess:.5f}\n")

# Finding the square root using the Newton-Raphson method
epsilon = 0.01
k = 54321
n = 0

if k < 0:
    print("Cannot compute the square root of a negative number.\n")
elif k == 0:
    print("Square root of 0 is 0.\n")
else:
    guess = k / 2.0  # More adaptable initial guess

    while abs(guess**2 - k) >= epsilon and n < 1000:
        guess -= (guess**2 - k) / (2 * guess)  # Newton-Raphson formula
        n += 1

    print(f"No. of guesses: {n}")
    print(f"Square root of {k} is close to {guess:.5f}\n")
ss
