#break Statement
mysum=0
for i in range(5, 11, 2):
    mysum+=i
    if mysum==5:
        break
        mysum+=1
print(mysum)


#Try it - Number of even numbers within  the range
e=0
for i in range(5): #i is 0,1,2,3,4
    if i%2==0:
        e+=1
print(e)
e=0
for i in range(10): #i is 0,1,2,3,4,5,6,7,8,9
    if i%2==0:
        e+=1
print(e)
e=0
for i in range(2,9,3): #i is 2,5,8
    if i%2==0:
        e+=1
print(e)
e=0
for i in range(-4,6,2): #i is -4,-2,0,2,4
    if i%2==0:
        e+=1
print(e)
e=0
for i in range(5,6): #i is 5
    if i%2==0:
        e+=1
print(e)


#Strings and Loops
#uses range to iterate through index of s
s="Demo loops - fruit loops"
for i in range(len(s)):
    if s[i]=='i' or s[i]=='u':
        print("There is an i or u")

#iterates through characters of s directly
for char in s:
    if char=='i' or char=='u':
        print("There is an i or u")

#iterates through characters of s directly(most "pythonic")
for char in s:
    if char in 'iu':
        print("There is an i or u")

#Robot cheerleaders
an_letters="aefhilmnorsxAEFHIMNORSX"

word=input("I will cheer for you! Enter a word: ")
times=int(input("Enthusiasm level (1-10): "))

for c in word:
          if c in an_letters:
              print(f'Give me an {c}: {c}')
          else:
              print(f'Give me a {c}: {c}')
print("What's that spell?")
for i in range(times):
    print(word,'!!!')

#Try it
s="abca"
seen=''
count=0
for char in s:
    if char not in seen:
        seen = seen+char
        count+=1
    else:
        pass #pass means do nothing
print(count)
print(len(seen)) #instead of using count variable




          
        


