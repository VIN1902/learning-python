# 3 components that python considers:
1. Iteration tools
- for, while, comprehension
2. Iterable
- string, lists, file, dictionary
3. Response
- __next__

# Working
- Iter tool asks iterable if it can work and sends a iter() method
- Iterable if allows sends a response as __next__ and the first item.
    - Iterable objects point to start of the contiguous memory location, not the entire thing.
    - this __next__ tells that 'you have got the first item, but more items are there just in next address that can have a iter() method.
- Iter tool after recieving next() keep calling iterable again-and-again to apply its method for contiguous data until end of the iterable.
- When last item of iterable is reached, a stop iteration exception is raised by iterable. That just tells that no more looping.

```py
# file is an iterable and readline() is an iteration tool with its own defined method.

# 1. Raw way
f = open('../requirements.txt')
f.__next__()
# keep calling this until each line of file is accessed.
# ...finally when every line is there: iterable raises an error.

# 2. Using readline method (an iteration tool)
f = open('../requirements.txt')
f.readline()
# keep calling this until each line of file is accessed.
# ...finally when every line is there: this time instead of error we get a nice empty string.
# behind the scene the iter tool is modifying and displaying that raised error in nice way.

# 3. Using for loop (an iteration tool)
for line in open('../requirements.txt'):
    print(line)

# at the end instead of an empty string this time we get nothing and everything is nicely formated.
# that's nothing but functionality defined for this specific iter tool.

# 4. using while (an iter tool) but works on the principle of readline
f = open('../requirements.txt')
while True:
    line = f.readline()
    if not line:
        break
    print(line, end='')

# if not line means if 'line' that, if f.readline() is evaluted as False (due to '' at last) then break the loop
# not operator just checks if the thing has a value inside it or not.
    # if no value then True else False

# 5. Making my own iter tool
my_list = [1,2,3,4,5]
i = iter(my_list)
# i has the first element of list and itself is an iterator
i.__next__()
# if print, shows 1 and succesive values on continous calls
# at the last item raises an error

# in case of f = open(), python behind the scene has set the iter(f), can confirm with 'iter(f) is f' or 'iter(f) is f.__next__()'
```

# Clarification
### Working of Iteration
- Iterator Requests an Item
    - The iteration tool (e.g., for loop) sends an iter() call to an iterable.
    - The iterable returns an iterator object (which has __next__()).
- Iterator Fetches Items
    - The iterator calls __next__() to get the next item.
    - This item is not the whole iterable but a reference to a memory location containing the item.
    - The iterator keeps fetching until it reaches the last item.
- End of Iteration
    - When no more items are left, StopIteration is raised.
    - Some iteration tools (like for loops) handle this exception internally to stop gracefully.
    - Others (like manual calls to __next__()) will raise an error if unchecked.
### Takeaway
- Iterable vs. Iterator:
    - An iterable can produce an iterator (iter(obj)).
    - An iterator is an object with __next__().
- For Loops Hide Complexity:
    - They call iter() and __next__() behind the scenes.
- readline() vs. __next__():
    - readline() stops gracefully with '', while __next__() raises an error.
- Custom Iterators Can Be Built:
    - Any object with __iter__() and __next__() can be an iterator.