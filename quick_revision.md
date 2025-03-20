# Keywords
- is / is not operator
- in / not in operator
- * and ** operator
- type()
- len()
- copy module

# Data
## Number
- type conv
- multiple value to variable
- chain comparison

- math
- random
- decimal

- base
- bitwise/logical operator

## string
- negative indexing
- methods: JR TRICSS PC [join, replace, trim, reverse, indexOf, case, slice, split, padStart/End, count]

## collections
- List = Array-like (JS Array, but allows duplicates)
- Dict = Object-like (JS Object, but ordered)
- Set = JS Set (No duplicates, unordered)
- Tuple = Immutable List (JS Array but frozen, like Object.freeze)
- methods: copy(), clear()
- unpacking/destructuring

## list
- IOCD (indexed, ordered, changable(mutable), duplication)
- negative indexing
- splice/slice
- concatination (+)
- append (push), pop (pop), insert (unshift), pop(0) (shift)
- list comprehension
- iteration: for value in list

## dict
- IOCDnot (indexed, ordered, changable(mutable), duplication not)
- access ([], get())
- pop('key')-> returns value, popitem()-> returns a sub-dict
- dict comprehension 
- iteration: for key, value in dict.items() OR for key in dict
- dict.fromkeys(keys, default_value)

## set
- InotOnotCnotDnot
- & (intersection()), | (union()), - (difference()), ^ (symmetric_difference())
- set(list)
- add, remove, discard, update
- set comprehension

## tuple
- IOCnotD
- negative indexing
- slice
- concatination (+)

## Common Collection Conversions

| Convert From | Convert To | Syntax |
|-------------|------------|--------|
| List → Set | Remove duplicates | `set(my_list)` |
| Set → List | Keep order (Python 3.7+) | `list(my_set)` |
| Dict → List of Keys | Default conversion | `list(my_dict)` |
| Dict → List of Values | Extract values | `list(my_dict.values())` |
| Dict → List of Tuples | Key-Value pairs | `list(my_dict.items())` |
| List of Tuples → Dict | Pairs to dictionary | `dict(my_list_of_tuples)` |