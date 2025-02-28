# Memory

## Primitive vs Non-primitive
- In programming languages, primitive and non-primitive types refer to how data is stored and manipulated in memory.
### Primitive:
- Primitive types are the most basic, built-in data types of a language.
- They usually store simple values (like numbers or characters).
- Typically, they are stored directly in the stack for fast access.
### Non-primitive:
- Non-primitive types are derived from primitive types and allow more complex structures.
- They typically store multiple values or objects (e.g., arrays, lists, dictionaries).
- Stored in the heap, with a reference (pointer) in the stack.

## Trends

1. Most Languages: Stack for Primitives, Heap for Objects

- Languages like C, C++, Java, and JavaScript follow a model where: Primitives (integers, floats, booleans, characters, etc.) are stored in the stack for efficiency. Non-primitive types (arrays, objects, strings, lists, etc.) are stored in the heap with a reference in the stack.

2. Python: Everything in Heap

- In Python, everything (even integers and booleans) is an object stored in the heap, with references (pointers) stored in the stack. The only exceptions are small integers (-5 to 256) and interned strings, which are cached for performance.

This extra level of indirection makes Python slower than languages that store primitives in the stack. Along with the fact that its an interpreted language. We can say mostly everything in python is non-primitive. But the trade off is it also makes python more flexible.

# Mutable vs Immutable
- In Python, objects are classified as mutable or immutable based on whether their values can be modified after creation.
## Immutable:
- Once created, immutable objects cannot be modified.
- Any operation that tries to modify an immutable object creates a new object instead of modifying the original one.
## Mutable:
- Mutable objects can be modified after creation without creating a new object.
- Operations modify the same memory location.

# DataType misconception
- In python there's no datatype of the variable you make, it only holds address to a memory space.
- But! the value at the memory address has a datatype. So 'type' belongs to the object not its reference.
- For numbers and strings GC works as usual but not immediately!
- Each object as its reference count. ref_count