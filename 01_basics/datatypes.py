# in python most things are 'objects', they store themselves in heap
# immutable -> no change -> can't change the refrence of object created

name = "vikas"
print(name)
name = "harsh"
# when redefined name then a new mem. space in heap created for value "harsh" and its address was stored in variable called 'name' in stack.
# so the previous address/reference of value "vikas" in heap is now no longer stored in 'name'. so the "vikas" object is orphaned and hence garbage collector will eventually delete it from heap
# here string type is immutable cause we never changed value "vikas", instead a new object was created on any reassignment and reference called 'name' now points to new object (stores address of it)


'''
# DataTypes:

- Immutable

1. int
2. float
3. str
4. bool
5. typle
6. frozenset
7. bytes

- Mutable

1. list
2. set
3. dict
4. bytearray
5. array
'''