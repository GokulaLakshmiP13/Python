#Guess-and-Check algorithm
#For positive input
guess = 0

x = int(input("Enter an integer: "))

while guess**2 < x:
    guess = guess + 1

if guess**2 == x:
    print("Square root of", x, "is", guess)
    print("So", x, "is a perfect square")
else:
    print(x, "is not a perfect square")

#For negative input
guess = 0
neg_flag=False
x = int(input("Enter an integer: "))
if x<0:
    neg_flag=True
while guess**2 < x:
    guess = guess + 1

if guess**2 == x:
    print("Square root of", x, "is", guess)
    print("So", x, "is a perfect squaree")
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print("Just checking... did you mean", -x, "?")


#Try it
secret=int(input("Enter the number: "))
for i in range(1,11): #i is 1,2,3,4,5,6,7,8,9,10
    if i==secret:
        print("The number is found")
   
#else print not found using boolean flag
found=False
secret=int(input("Enter the number: "))
for i in range(1,11): #i is 1,2,3,4,5,6,7,8,9,10
    if i==secret:
        print("The number is found")
        found=True
if not found:
    print("The number  is not found")
        

#Guess and Check cube root
#Positive cubes
cube=int(input("Enter an integer: "))
for guess in range(cube+1):
    if guess**3==cube:
        print("The cube root of ", cube, "is", guess)

#Negative cubes
cube=int(input("Enter an integer: "))
for guess in range(abs(cube)+1):  #The absolute value of a number is its non-negative value, regardless of its sign
    if guess**3==cube:
        if cube<0:
            guess=-guess  #Deal with negative cube here    
        print("The cube root of ", cube, "is", guess)

#Just a little faster
cube = int(input("Enter an integer: "))
for guess in range(abs(cube) + 1):
    # Terminate search once you know you have passed possible answer
    if guess**3 >= abs(cube):
        break
# Check why you exited the loop and decide if the guess is not a perfect cube
if guess**3 != abs(cube):
    print(cube, "is not a perfect cube")
else:
    if cube < 0:
        guess = -guess
    print("Cube root of " + str(cube) + " is " + str(guess))

#Word problem
for alyssa in range(11):  
    for ben in range(11):  
        for cindy in range(11):  

            total = (alyssa + ben + cindy == 10)  
            two_less = (ben == alyssa - 2)  
            twice = (cindy == 2 * alyssa)  

            if total and two_less and twice:  
                print(f"Alyssa sold {alyssa} tickets")  
                print(f"Ben sold {ben} tickets")  
                print(f"Cindy sold {cindy} tickets")

#For largest numbers
for alyssa in range(1001):  
    ben = max(alyssa - 20, 0)  # Ben's tickets must be at least 0  
    cindy = alyssa * 2  # Cindy's tickets are twice Alyssa's  

    if ben + cindy + alyssa == 1000:  
        print("Alyssa sold " + str(alyssa) + " tickets")  
        print("Ben sold " + str(ben) + " tickets")  
        print("Cindy sold " + str(cindy) + " tickets")


#Binary Numbers
x = 0

for i in range(10):
    x += 0.1

print(x == 1)
print(x, "==", 10 * 0.1)

#Decimal to binary conversions
num=int(input("Enter an integer: "))
result = ''

if num == 0:
    result = '0'

while num > 0:
    result = str(num % 2) + result
    num = num // 2
print(result)

#For negative numbers
num=int(input("Enter an integer: "))
if num < 0:
    is_neg = True
    num = abs(num)
else:
    is_neg = False

result = ''

if num == 0:
    result = '0'

while num > 0:
    result = str(num % 2) + result
    num = num // 2

if is_neg:
    result = '-' + result

print(result)
