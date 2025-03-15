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
list_four = [4,5,6]
# even though it looks same but a new object is created at 0x3 and that is now stored in 'list_four'
list_three[0] = 69
# list is mutuable at 0x2
print(list_three) # [69,5,6] at 0x2
print(list_four) # [4,5,6] at 0x3

name = "vikas"
print(name)
name = "harsh"
# when redefined name then a new mem. space in heap created for value "harsh" and its address was stored in variable called 'name' in stack.
# so the previous address/reference of value "vikas" in heap is now no longer stored in 'name'. so the "vikas" object is orphaned and hence garbage collector will eventually delete it from heap
# here string type is immutable cause we never changed value "vikas", instead a new object was created on any reassignment and reference called 'name' now points to new object (stores address of it)