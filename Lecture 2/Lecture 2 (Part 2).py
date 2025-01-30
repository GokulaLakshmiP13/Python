# F Strings (Formatted Strings)
num = 3000
fraction = 1 / 3
print(num * fraction, 'is', fraction * 100, '% of', num)  # Output: 1000.0 is 33.33333333333333 % of 3000
print(num * fraction, 'is', str(fraction * 100) + '% of', num)  # Output: 1000.0 is 33.33333333333333% of 3000
# Expressions in curly braces evaluated at runtime, automatically converted to strings, and concatenated to the string preceding them
print(f'{num * fraction} is {fraction * 100}% of {num}')  # Output: 1000.0 is 33.33333333333333% of 3000

# Comparison operators
print('a' == 'A')  # Output: False
print(2 < 3)  # Output: True
print(not (2 < 3))  # Output: False

# Comparison with logical operator
print((2 < 3) and (3 < 4))  # Output: True
print((2 < 3) and (3 > 4))  # Output: False

pset_time = 15
sleep_time = 8
print(sleep_time > pset_time)  # Output: False

derive = True
drink = False
both = drink and derive
print(both)  # Output: False

# Write a program that:
# 1. Saves a secret number in a variable
# 2. Asks the user for a number guess
# 3. Prints a bool False or True depending on whether the guess matches the secret
secret = 5
guess = int(input("Please guess a number: "))  # Example: Please guess a number: 4
print(secret == guess)  # Output: False

# Another method
e = print(secret == guess)  # Output: False
