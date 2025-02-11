#Conversions: Decimal to Binary
x = 0.625
p = 0

# Check if the value of x is greater than 1
while ((2 ** p) * x)%1 !=0:
    print('Remainder= ' + str((2**p)*x - int((2**p)*x)))
    p += 1

num = int(x * (2 ** p))

result = ''

if num == 0:
    result = '0'

while num > 0:
    result = str(num % 2) + result
    num = num // 2

# Add leading zeros if necessary
for i in range(p - len(result)):
    result = '0' + result

# Truncate the result by removing excess digits
result = result[0:-p] + '.' + result[-p:]

print('The binary representation of the decimal ' + str(x) + ' is ' + str(result))


#Guess and check: Square root
x = 36  # Number to find the square root of
epsilon = 0.01  # Precision level
num_guesses = 0  # Counter for the number of guesses
guess = 0.0  # Initial guess
increment = 0.0001  # Step size for incremental search

# Prevent infinite loops by setting a reasonable upper limit for guess
max_iterations = 1000000  # Safety limit

while abs(guess**2 - x) >= epsilon and num_guesses < max_iterations:
    guess += increment
    num_guesses += 1

print(f"num_guesses: {num_guesses}")
print(f"{guess:.5f} is close to the square root of {x}")


x = 54321  # Number to find the square root of
epsilon = 0.01  # Precision level
n = 0  # Counter for number of guesses
guess = 0  # Initial guess
increment = 0.0001  # Step size for incremental search

# Prevent infinite loops by setting a reasonable upper limit
max_iterations = 10000000  # Safety limit

while abs(guess**2 - x) >= epsilon and guess <= x and n < max_iterations:
    guess += increment
    n += 1

print(f"No. of guesses: {n}")

if guess**2 > x:  # Check if we exceeded x without finding a close answer
    print("Cannot find square root of", x)
    print("Last guess was", guess, "and its square is", guess**2)
else:
    print(f"Square root of {x} is close to {guess:.5f}")
