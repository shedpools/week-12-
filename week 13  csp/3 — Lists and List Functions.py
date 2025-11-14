# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
#collections are used to store multiple items in a single variable
# lists are ordered collections of items
#lists are mutable meaning you can change their content
#lists are created using square brackets []
# my_list = [1,2,3,4,5]
# print(my_list) # 1 2 3 4 5
# print(type(my_list)) #class 'list'
# print(my_list[0]) #1
# print(my_list[1:4]) #[2,3,4]
# print(my_list[0:]) # [1,2,3,4,5]
# my_list.append(6)
# print(my_list) #]1,2,3,4,5,6]
# my_list.extend([10,11,12,13,14])
# my_list.extend(list(range(15,1000)))
# print(my_list) 


new_list = ['a', 'b' , 'c']
print(new_list) 
new_list.append('d')
print(new_list)
#remove item from list
removed_item = new_list.pop()
#removes last itme by default
print(removed_item)
print(new_list)
remove_second_item = new_list.pop(1)
print(remove_second_item)
print(new_list)

numbers = [4,2,5,1,3]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.insert(2,10)
print(numbers)
numbers.insert(2,10)
print(numbers)
third_list = [7,8,9]
third_list[0] = 6
print(third_list)
third_list[-1] = 10
print(third_list)
import random
random_list = random.sample(range(1,100),10)
print(random_list)
print(sorted(random_list))
sorted_list = sorted(random_list)
print(sorted_list)
#instead of creatin seperate variables
#for each item we can store them in a list
#this makes our job easier because when we meed to manage multiple items 
#performance task answer

# Examples:

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.