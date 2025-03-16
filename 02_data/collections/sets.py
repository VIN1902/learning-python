# mutable
# unordered, unchangeable (add or remove is allowed), and unindexed (can't acess value).

set_one = {1,2,3}
set_two = {3,4,5}

print(set_one & set_two) # or use .intersection()
print(set_one | set_two) # or use .union()
print(set_one - set_one) # or use .difference() ; {}❌, set()✅
print(set_one ^ set_two) # or use symmetric_difference()

list = ['a', 'b', 'c', 'a']
set_from_list = set(list)
print(set_from_list)

# access - can't use indexing instead loop through
for value in set_one:
    print(value)

# add/remove
set_one.add(69)
set_one.update(set_two)
set_one.remove(1)
set_one.discard(99) # discard doen't raise an error if the specified value doesn't exit; unlike remove.
print(set_one)