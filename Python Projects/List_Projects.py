#List Practice. 17:17

#Method1 to take input as list
num_list = input("Enter the list of numbers: ").split()
print(num_list)

#Method2 to take input as list withput spaces eg:1234 = [1,2,3,4]
num_list2 = list(input("ENter the number: "))
print(num_list2)

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
print(f"Test for clear list: {num_list.clear()}") #removes all elements from a list.
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

