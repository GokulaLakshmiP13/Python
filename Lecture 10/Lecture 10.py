L = [2, 4, 8]  
print(L)  

# Adding an element to the list using append()  
L.append(9)  
print(L)  

L1 = ['re']  
L2 = ['mi']  
L3 = ['do']  

# Concatenating two lists  
L4 = L1 + L2  # L4 becomes ['re', 'mi']  

# Adding a list inside another list  
L3.append(L4)  # L3 becomes ['do', ['re', 'mi']]  

# Modifying L1 by appending L3 (L1 is changed in-place, L is set to None)  
L = L1.append(L3)  # L1 becomes ['re', ['do', ['re', 'mi']]], L is None  

def make_ordered_list(n):  
    """
    Generates a list containing elements from 0 to n in ascending order.
    :param n: A positive integer.
    :return: A list of numbers from 0 to n.
    """  
    L = []  
    for i in range(n + 1):  
        L.append(i)  
    return L  

print("Creating an ordered list:")  
L1 = make_ordered_list(5)  
print(L1)  

def remove_elem(L, e):  
    """
    Removes all occurrences of a specific element from the list.
    :param L: A list of elements.
    :param e: The element to be removed.
    :return: A new list with the specified element removed.
    """  
    L1 = []  
    for i in L:  
        if i != e:  
            L1.append(i)  
    return L1  

print("Removing an element from the list:")  
L = [1, 2, 2, 2, 3]  
print(remove_elem(L, 2))  

# Splitting a sentence into words using split()  
print("Splitting a sentence into a list of words:")  
s = "Hello World "  
List = s.split()  
print(List)  

# Joining words in a list to form a string  
print("Converting a list back into a string:")  
str = " ".join(List)  
print(str)  

def count_words(sen):  
    """
    Counts the number of words in a sentence.
    :param sen: A string containing a sentence.
    :return: The total number of words.
    """  
    word_list = sen.split()  
    return len(word_list)  

print("Counting words in the sentence: 'Hello there How are you?'")  
print(count_words("Hello there How are you?"))  

def sort_words(sen):  
    """
    Sorts the words in a sentence alphabetically.
    :param sen: A sentence in string format.
    :return: A list of words arranged in alphabetical order.
    """  
    words_list = sen.split()  
    words_list.sort()  
    return words_list  

print("Sorting words in the sentence: 'look at this photograph'")  
print(sort_words("look at this photograph"))  

def square_list(L):  
    """
    Modifies the list by squaring each element.
    :param L: A list of integers.
    :return: The updated list where each element is squared.
    """  
    for i in range(len(L)):  
        L[i] = L[i] ** 2  
    return L  

print("Squaring each element in the list: [1, 3, 5, 9]")  
print(square_list([1, 3, 5, 9]))  

L = [1, 2, 3, 4]  
print("Tricky case 1 - Appending elements inside a loop:")  
for i in range(len(L)):  
    L.append(i)  
    print(L)  

# This will cause an infinite loop, so it's commented out  
# print("Tricky case 2 - Infinite loop caused by appending inside iteration")  
# L = [1, 2, 3, 4]  
# i = 0  
# for e in L:  
#     L.append(i)  
#     i += 1  
#     print(L)  

# Using extend() to add multiple elements at the end of the list  
print("Tricky case 3 - Extending a list with multiple elements:")  
L1 = [1, 6, 9]  
L1.extend([0, 7])  
print(L1)  

L = [1, 2, 3, 4]  
print("Tricky case 4 - Expanding the list within a loop:")  
for e in L:  
    L = L + L  
    print(L)  

# Clearing all elements from the list  
print("Clearing the list:")  
L.clear()  
print(L)  
