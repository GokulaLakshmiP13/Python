# Types of scalar objects
type(7)
<class 'int'>
type(3.0)
<class 'float'>
type(True)
<class 'bool'>
type(False)
<class 'bool'>
type(1234)
<class 'int'>
type(8.99)
<class 'float'>
type(9.0)
<class 'float'>
# Type Casting (Convert one type to another)
float(3)
int(5.2)
int(5.9)
round(5.9)
float(123)
round(7.9)
float(round(7.2))
int(7.2)
int(7.9)

# Expression
3 + 2
(4 + 2) * 6 - 1
type((4 + 2) * 6 - 1)
float((4 + 2) * 6 - 1)
(13 - 4) / (12 * 12)
type(4 * 3)
type(4.0 * 3)
int(1 / 2)
5 / 3
5 // 3 # Floor division
5 % 3

# Which of these are allowed in Python?
# Assignment - (variable = value)
x = 6
# 6 = x  # SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
# x * y = 3 + 4  # SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
xy = 3 + 4
xy
xy + 1

pi = 355 / 113
radius = 2.2
area = pi * (radius * 2)
circumference = pi * (radius * 2)

# Best code style
a = 355 / 133 * (2.2 * 2)
c = 355 / 133 * (2.2 * 2)

# Instead of reusing
a = c

# Executed in order - what are the values of meters and feet variables at each line in the code
meters = 100
feet = 3.2802 * meters
meters = 200
feet
meters

# Swap values of x and y without binding the numbers directly
x = 1
y = 2
y = x
y
x = y
x
y = 2
y = x
# x = temp  # NameError: name 'temp' is not defined
x = 1
y = 2
temp = y
y = x
x = temp
x
y

