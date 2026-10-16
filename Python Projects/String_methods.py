print("Hello Vanitha")
test_str = input("Enter the string: ")
print(f"Test for caps string: {test_str.upper()}") #Capitalizes all letters in a string.
print(f"Test for lowercase string: {test_str.lower()}") #low case all letters in a string.
print(f"Test for title string: {test_str.title()}") #capitalizes all 1st letters of each word in a sentence.    
print(f"Test for title string: {test_str.capitalize()}") #capitalizes only 1st letter of a sentence. 

print(f"Test for find string: {test_str.find('the')}") #finds the index of the first occurrence of a substring in a string.

print(f"Test for count string: {test_str.count('the')}") #counts the number of occurrences of a substring in a string.

print(f"Test for replace string: {test_str.replace('the', 'THE')}") #replaces all occurrences of a substring with another substring.

print(f"Test for split string: {test_str.split()}") #splits a string into a list of substrings based on whitespace.

print(f"Test for strip string: {test_str.strip()}") #removes leading and trailing whitespace from a string.

print(f"Test for isalpha string: {test_str.isalpha()}") #checks if all characters in a string are alphabetic.

print(f"Test for isdigit string: {test_str.isdigit()}") #checks if all characters in a string are digits.

print(f"Test for isspace string: {test_str.isspace()}") #checks if all characters in a string are whitespace.

print(f"Test for startswith string: {test_str.startswith('Hello')}") #checks if a string starts with a specified substring.

print(f"Test for endswith string: {test_str.endswith('World')}") #checks if a string ends with a specified substring.

print(f"Test for join string: {'-'.join(test_str)}") #joins the elements of an iterable (like a list) into a single string, with a specified separator.

print(f"Test for len string: {len(test_str)}") #returns the length of a string.

print(f"Test for index string: {test_str.index('the')}") #returns the index of the first occurrence of a substring in a string.

print(f"Test for isalnum string: {test_str.isalnum()}") #checks if all characters in a string are alphanumeric (letters and numbers).

print(f"Test for swapcase string: {test_str.swapcase()}") #swaps the case of all letters in a string (uppercase to lowercase and vice versa).

print(f"Test for zfill string: {test_str.zfill(20)}") #pads a string with zeros on the left, to fill a specified width.

print(f"Test for center string: {test_str.center(20, '*')}") #centers a string within a specified width, padding with a specified character.

print(f"Test for lstrip string: {test_str.lstrip()}") #removes leading whitespace from a string.

print(f"Test for rstrip string: {test_str.rstrip()}") #removes trailing whitespace from a string.

print(f"Test for partition string: {test_str.partition('the')}") #splits a string into three parts: the part before the separator, the separator itself, and the part after the separator.

print(f"Test for rpartition string: {test_str.rpartition('the')}") #splits a string into three parts: the part before the last occurrence of the separator, the separator itself, and the part after the separator.

print(f"Test for expandtabs string: {test_str.expandtabs(4)}") #replaces tab characters in a string with spaces, using a specified tab size.

print(f"Test for isdecimal string: {test_str.isdecimal()}") #checks if all characters in a string are decimal characters.
print(f"Test for isidentifier string: {test_str.isidentifier()}") #checks if a string is a valid identifier in Python.
print(f"Test for isprintable string: {test_str.isprintable()}") #checks if all characters in a string are printable.
print(f"Test for islower string: {test_str.islower()}") #checks if all characters in a string are lowercase.
print( f"Test for isupper string: {test_str.isupper()}") #checks if all characters in a string are uppercase.
print(f"Test for istitle string: {test_str.istitle()}") #checks if a string is in title case (first letter of each word is uppercase).
print(f"Test for isspace string: {test_str.isspace()}") #checks if all characters in a string are whitespace.






"""
#-----------------OUTPUT------------------------------
Hello Vanitha
Enter the string: This is the test for the string methods
Test for caps string: THIS IS THE TEST FOR THE STRING METHODS
Test for lowercase string: this is the test for the string methods
Test for title string: This Is The Test For The String Methods
Test for title string: This is the test for the string methods
Test for find string: 8
Test for count string: 2
Test for replace string: This is THE test for THE string methods
Test for split string: ['This', 'is', 'the', 'test', 'for', 'the', 'string', 'methods']
Test for strip string: This is the test for the string methods
Test for isalpha string: False
Test for isdigit string: False
Test for isspace string: False
Test for startswith string: False
Test for endswith string: False
Test for join string: T-h-i-s- -i-s- -t-h-e- -t-e-s-t- -f-o-r- -t-h-e- -s-t-r-i-n-g- -m-e-t-h-o-d-s
Test for len string: 39
Test for index string: 8
Test for isalnum string: False
Test for swapcase string: tHIS IS THE TEST FOR THE STRING METHODS
Test for zfill string: 00000000000000000000000000000000000000000This is the test for the string methods
Test for center string: ********************This is the test for the string methods*********************
Test for lstrip string: This is the test for the string methods
Test for rstrip string: This is the test for the string methods
Test for partition string: ('This is ', 'the', ' test for the string methods')
Test for rpartition string: ('This is the test for ', 'the', ' string methods')
Test for expandtabs string: This is the test for the string methods
Test for isdecimal string: False
Test for isidentifier string: False
Test for isprintable string: True
Test for islower string: False
Test for isupper string: False
Test for istitle string: False
Test for isspace string: False
#-------------------------------------------------------------------------------------------------------------
"""
