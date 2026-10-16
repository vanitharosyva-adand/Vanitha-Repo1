#List Practice. 

#Method1 to take input as list
num_list = input("Enter the list of numbers: ").split()
print(num_list)
print(f"Type of num_list: {type(num_list)}")


#Method2 to take input as list withput spaces eg:1234 = [1,2,3,4]
num_list2 = list(input("ENter the number: "))
print(num_list2)
print(f"Type of num_list2: {type(num_list2)}")

#-------------------------
list2 = []
list2.append('2')
list2.extend(['3','6'])
print(list2)
#-------------------------



#print(reversed(num_list)) #reverses the order of elements in a list.

print(f"Test for sort list: {sorted(num_list)}") #sorts the elements of a list in ascending order.
print(f"Test for reverse list: {list(reversed(num_list))}") #revers es the order of elements in a list.
print(f"Test for append list: {num_list.append('5')} {num_list}") #adds an element to the end of a list.
print(f"Test for extend list: {num_list.extend(['6', '7'])} {num_list}") #adds multiple elements to the end of a list.
print(f"Test for insert list: {num_list.insert(2, '8')} {num_list}") #inserts an element at a specified index in a list.
print(f"Test for remove list: {num_list.remove('5')} {num_list}") #removes the first occurrence of a specified element from a list.
print(f"Test for pop list: {num_list.pop()} {num_list}") #removes and returns  the last element of a list.
print(f"Test for index list: {num_list.index('3')}") #returns the   index of the first occurrence of a specified element in a list.
print(f"Test for count list: {num_list.count('3')}") #counts the number of occurrences of a specified element in a list.

print(f"Test for copy list: {num_list.copy()}") #creates a shallow copy of a list.  
print(f"Test for len list: {len(num_list)}") #returns the number of elements in a list. 
print(f"Test for max list: {max(num_list)}") #returns the maximum value from a list.
print(f"Test for min list: {min(num_list)}") #returns the minimum value from a list.
print(f"Test for sum list: {sum(map(int, num_list))}") #returns the sum of all elements in a list.  
print(f"Test for any list: {any(map(int, num_list))}") #returns True if any element in a list is true.
print(f"Test for all list: {all(map(int, num_list))}") #returns True if all elements in a list are true.
print(f"Test for sorted list: {sorted(num_list)}") #returns a new sorted list from the elements of a list.  
print(f"Test for reversed list: {list(reversed(num_list))}") #returns a new reversed list from the elements of a list.  
print(f"Test for enumerate list: {list(enumerate(num_list))}") #returns an enumerate object that contains pairs of index and value for each element in a list.  
print(f"Test for zip list: {list(zip(num_list, num_list2))}") #returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the input lists.  
print(f"Test for filter list: {list(filter(lambda x: int(x) > 2, num_list))}") #returns a new list containing elements that satisfy a specified condition.  
print(f"Test for map list: {list(map(lambda x: int(x) * 2, num_list))}") #returns a new list containing the results of applying a specified function to each element in a list. 
# print(f"Test for reduce list: {from functools import reduce; reduce(lambda x, y: int(x) + int(y), num_list)}") #returns a single value that is the result of applying a specified function cumulatively to the elements of a list.  
print(f"Test for list comprehension: {[int(x) ** 2 for x in num_list]}") #returns a new list containing the results of applying a specified expression to each element in a list.   
print(f"Test for list slicing: {num_list[1:4]}") #returns a new list containing a subset of elements from a list, specified by a start and end index.   
print(f"Test for list slicing with step: {num_list[::2]}") #returns a new list containing every n-th element from a list, specified by a step value.    
print(f"Test for list slicing with negative step: {num_list[::-1]}") #returns a new list containing the elements of a list in reverse order.    
print(f"Test for list slicing with negative step and start index: {num_list[3::-1]}") #returns a new list containing the elements of a list in reverse order, starting from a specified index.  
print(f"Test for list slicing with negative step and end index: {num_list[:-3:-1]}") #returns a new list containing the elements of a list in reverse order, ending at a specified index.   
print(f"Test for list slicing with negative step and start and end index: {num_list[3:1:-1]}") #returns a new list containing the elements of a list in reverse order, starting and ending at specified indices.    
print(f"Test for list slicing with negative step and start and end index and step: {num_list[3:1:-2]}") #returns a new list containing the elements of a list in reverse order, starting and ending at specified indices, with a specified step value.  
print(f"Test for list slicing with negative step and start and end index and step and negative step: {num_list[3:1:-2]}") #returns a new list containing the elements of a list in reverse order, starting and ending at specified indices, with a specified step value.    
print(f"Test for list slicing with negative step and start and end index and step and negative step and start index: {num_list[3:1:-2]}") #returns a new list containing the elements of a list in reverse order, starting and ending at specified indices, with a specified step value.    
print(f"Test for list slicing with negative step and start and end index and step and negative step and start index and end index: {num_list[3:1:-2]}") #returns a new list containing the elements of a list in reverse order, starting and ending at specified indices, with a specified step value.  
print(f"Test for clear list: {num_list2.clear()}") #removes all elements from a list.


#------------------------------------/
#Take a list of numbers from the user and print the sum.
num_list3 = input("Enter the list elements separated by space: ").split()
total = sum(int(x) for x in num_list3)
print(f"The sum of the numbers is: {total}")
#------------------------------------/
#List sorting: Take a list of numbers from the user and print the sorted list.
sorted_list = sorted(num_list3)
print(f"The sorted list is: {sorted_list}")
#------------------------------------/
#List Reverse
reversed_list = list(reversed(num_list))
print(f"Reversed list is: {reversed_list}")
#----------------------------------------/
#List slicing: Take a list of numbers from the user and print the sliced list.
new2 = num_list[::-1]
print(f"new2 content is: {new2}")
#-----------------------------------
max_num = max(num_list)
print(f"Max of {num_list} is = {max_num}")
#-----------------------------------
#--Odd or even 
print(["even" if int(x) % 2 == 0 else "Odd" for x in num_list])



"""
#---------------------OUTPUT-----------------------
Enter the list of numbers: 1 2 5 4 3
['1', '2', '5', '4', '3']
Type of num_list: <class 'list'>
ENter the number: 54351
['5', '4', '3', '5', '1']
Type of num_list2: <class 'list'>
['2', '3', '6']
Test for sort list: ['1', '2', '3', '4', '5']
Test for reverse list: ['3', '4', '5', '2', '1']
Test for append list: None ['1', '2', '5', '4', '3', '5']
Test for extend list: None ['1', '2', '5', '4', '3', '5', '6', '7']
Test for insert list: None ['1', '2', '8', '5', '4', '3', '5', '6', '7']
Test for remove list: None ['1', '2', '8', '4', '3', '5', '6', '7']
Test for pop list: 7 ['1', '2', '8', '4', '3', '5', '6']
Test for index list: 4
Test for count list: 1
Test for copy list: ['1', '2', '8', '4', '3', '5', '6']
Test for len list: 7
Test for max list: 8
Test for min list: 1
Test for sum list: 29
Test for any list: True
Test for all list: True
Test for sorted list: ['1', '2', '3', '4', '5', '6', '8']
Test for reversed list: ['6', '5', '3', '4', '8', '2', '1']
Test for enumerate list: [(0, '1'), (1, '2'), (2, '8'), (3, '4'), (4, '3'), (5, '5'), (6, '6')]
Test for zip list: [('1', '5'), ('2', '4'), ('8', '3'), ('4', '5'), ('3', '1')]
Test for filter list: ['8', '4', '3', '5', '6']
Test for map list: [2, 4, 16, 8, 6, 10, 12]
Test for list comprehension: [1, 4, 64, 16, 9, 25, 36]
Test for list slicing: ['2', '8', '4']
Test for list slicing with step: ['1', '8', '3', '6']
Test for list slicing with negative step: ['6', '5', '3', '4', '8', '2', '1']
Test for list slicing with negative step and start index: ['4', '8', '2', '1']
Test for list slicing with negative step and end index: ['6', '5']
Test for list slicing with negative step and start and end index: ['4', '8']
Test for list slicing with negative step and start and end index and step: ['4']
Test for list slicing with negative step and start and end index and step and negative step: ['4']
Test for list slicing with negative step and start and end index and step and negative step and start index: ['4']
Test for list slicing with negative step and start and end index and step and negative step and start index and end index: ['4']
Test for clear list: None
Enter the list elements separated by space: 1 4 3 2
The sum of the numbers is: 10
The sorted list is: ['1', '2', '3', '4']
Reversed list is: ['6', '5', '3', '4', '8', '2', '1']
new2 content is: ['6', '5', '3', '4', '8', '2', '1']
Max of ['1', '2', '8', '4', '3', '5', '6'] is = 8
['Odd', 'even', 'even', 'even', 'Odd', 'Odd', 'even']
#------------------------------------------------------------------
"""
