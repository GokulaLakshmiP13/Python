# Printing the output using print command
a = "the"
b = 3
c = "musketeer"
print(a, b, c)  # Output: the 3 musketeer

print(a + str(b) + c)  # Output: the3musketeer
# To concatenate, all variables should be of the same type so b is converted to string by type casting

# Input command
text = input("Type anything: ")  # Example: Type anything: Hellow
print(5 * text)  # Output: HellowHellowHellowHellowHellow

# input always returns a str, must cast if working with numbers
num1 = input("Type a number: ")  # Example: Type a number: 5
print(5 * num1)  # Output: 55555

num2 = int(input("Type a number: "))  # Example: Type a number: 5
print(5 * num2)  # Output: 25

# Write a program that:
# 1. Asks the user for a verb
# 2. Prints "I can <verb> better than you"
# 3. Then prints the verb 5 times in a row, separated by spaces
question = input('Choose a verb: ')  # Example: Choose a verb: write
print('I can', question, 'better than you!')  # Output: I can write better than you!
print(question * 5)  # Output: writewritewritewritewrite

# Try Newton Raphson for cube root
x = int(input('What x to find the cube root of? '))  # Example: What x to find the cube root of? 3
g = int(input('What guess to start with? '))  # Example: What guess to start with? 4
print('Current estimated cubed =', g**3)  # Output: Current estimated cubed = 64
next_g = g - ((g**3 - x) / (3 * g**2))
print('Next guess to try =', next_g)  # Output: Next guess to try = 2.729166666666667

