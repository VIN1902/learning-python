list_one = [1,2,3]
# new object created of list type and its address (say 0x1) stored in 'list_one' which is in stack
list_two = list_one
# the address of '[1,2,3]' is now in both list_one and list_two
list_one[0] = 69
# list are mutable, so no new object created and the value changed at 0x1 list type
print(list_one) # [69,2,3]
print(list_two) # [69,2,3]

list_three = [4,5,6]
# new obj created at address (say 0x2) and that is stored in 'list_three' in stack
list_four = list_three
# both have address 0x2 in them
list_three = [4,5,6]
# even though it looks same but a new object is created at 0x3 and that is now stored in 'list_three'
list_three[0] = 69
# list is mutuable at 0x3
print(list_three) # [69,5,6] at 0x3
print(list_four) # [4,5,6] at 0x2

name = "vikas"
print(name)
name = "harsh"
# when redefined name then a new mem. space in heap created for value "harsh" and its address was stored in variable called 'name' in stack.
# so the previous address/reference of value "vikas" in heap is now no longer stored in 'name'. so the "vikas" object is orphaned and hence garbage collector will eventually delete it from heap
# here string type is immutable cause we never changed value "vikas", instead a new object was created on any reassignment and reference called 'name' now points to new object (stores address of it)

score = 10
new_score = 10
print(score == new_score)
print(score is new_score)
# both pointers score and new_score hold the same address to a memory space where value of integer 10 is stored.
# internally a ref_count is stored to keep track of how many references does a single object has.

# memory's stored value has a datatype but python in general when talking about stack variables doesn't have a datatype.
# GC doesn't work immediately on orphaned number and string data in memory space.

# before calculation all the references are replaced by their value and then after calculation a new object is made and its memory address is assigned to the previous variable.
# ex: a = 5, b = 2, a = a + 2, -> a = 5 + 2 -> a = 7 (7 is a new object), after a while '5' object will be collected.

l1 = [7,8,9]
l2 = l1[:] # slice creates a shallow copy, a new object from subset of original object
l1[0] = 999
print(l1)
print(l2)

import copy

original = [1, 2, 3, [4, 5, 6], 7, 8, 9]

# Create copies
shallow_copy = copy.copy(original)  # Shallow copy
deep_copy = copy.deepcopy(original)  # Deep copy

# Modify a nested element in the original list
original[3][0] = 99

# Print to observe changes
print("Original:", original)          
print("Shallow Copy:", shallow_copy)  
print("Deep Copy:", deep_copy)        
# Shallow Copy (copy.copy()): Creates a new object, but references nested mutable objects (like lists) from the original. If the original is modified inside a nested structure, the shallow copy will reflect those changes.
# Deep Copy (copy.deepcopy()): Recursively copies all objects, creating independent copies of nested mutable objects. Changes to the original won't affect the deep copy.