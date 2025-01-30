# Branching
pset_time = 22
sleep_time = 1

if (pset_time + sleep_time) > 24:
    print("impossible!")
elif (pset_time + sleep_time) == 24:
    print("full schedule!")
else:
    leftover = abs(24 - (pset_time + sleep_time))
    print(leftover, "h of free time!")  # Output: 2 h of free time!

print("end of day")  # Output: end of day

# You try it!
x = int(input("Enter a number for x: "))  # Example input: 5
y = int(input("Enter a different number for y: "))  # Example input: 7

if x == y:
    print(x, "is the same as", y)
    print("These are equal!")
else:
    print(x, "is different from", y)

# Indentation and Nested branching
x = float(input("Enter a number for x: "))  # Example input: 5.5
y = float(input("Enter a number for y: "))  # Example input: 3.2

if x == y:
    print("x and y are equal")
    if y != 0:
        print("Therefore, x/y is", x / y)
elif x < y:
    print("x is smaller")  # Output: x is smaller (if x is smaller than y)
else:
    print("y is smaller")  # Output: y is smaller (if y is larger than x)

print("Thanks!")  # Output: Thanks!

# You try it (Write a program that):
# 1. Saves a secret number.
# 2. Asks the user for a number guess.
# 3. Prints whether the guess is too low, too high, or the same as the secret.
secret = 5
guess = int(input("Guess a num: "))  # Example input: 4

if guess > secret:
    print("too high")  # Output: too high (if guess is greater than secret)
elif guess == secret:
    print("Equal")  # Output: Equal (if guess is equal to secret)
else:
    print("too low")  # Output: too low (if guess is smaller than secret)
