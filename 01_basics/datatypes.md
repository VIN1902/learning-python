# Why confusion online resources on python datatypes

- Python has built-in types, standard library types, and abstract types, and different sources mix them up.

# Built-in Types

## Immutable

1. Numeric Types

- int -> Integer numbers (e.g., 42, -5)
- float -> Floating-point numbers (e.g., 3.14, -0.001)
- complex -> Complex numbers (e.g., 3 + 4j)
- bool -> Boolean values (True, False), subclass of int

2. String & Byte Types

- str -> Unicode text (e.g., "hello", "Python")
- bytes -> Immutable byte sequences (e.g., b'hello')

3. Tuple & Frozen Set

- tuple -> Ordered, immutable sequence (e.g., (1, 2, 3))
- frozenset -> Immutable set (e.g., frozenset({1, 2, 3}))

4. NoneType

- None -> Represents "nothing" or "absence of a value"

## Mutable

5. Sequence & Collection Types

- list -> Ordered, mutable sequence (e.g., [1, 2, 3])
- set -> Unordered, mutable collection of unique items (e.g., {1, 2, 3})
- dict -> Key-value pairs, mutable (e.g., {"a": 1, "b": 2})

6. Bytearray Type

- bytearray -> Mutable sequence of bytes (e.g., bytearray(b'hello'))

⭐ The memoryview datatype also works as if its built-in, BUT not said to be one officially...
```py
name = b"Vikas Indora"
print(memoryview(name))
# Output: <memory at 0x0000018A3EBE1A80>
```

# Standard Library Types

- Python’s standard library provides extra data structures beyond built-in types.

| Type              | Module        | Description                                                                 |
| ----------------- | ------------- | --------------------------------------------------------------------------- |
| `deque`           | `collections` | A **double-ended queue**, optimized for fast appends/pops.                  |
| `defaultdict`     | `collections` | A `dict` that provides a default value for missing keys.                    |
| `OrderedDict`     | `collections` | A `dict` that remembers insertion order (Python 3.7+ does this by default). |
| `Counter`         | `collections` | A dict subclass for counting hashable items.                                |
| `NamedTuple`      | `collections` | An immutable, lightweight class with named fields.                          |
| `dataclass`       | `dataclasses` | A class that auto-generates `__init__`, `__repr__`, etc.                    |
| `Path`            | `pathlib`     | Object-oriented file system paths.                                          |
| `Queue`           | `queue`       | Thread-safe FIFO queue.                                                     |
| `SimpleNamespace` | `types`       | Like a dict, but allows attribute-style access.                             |

# Abstract Base Class

- ABCs define common interfaces that different data structures can implement. These aren't real data types but provide a way to check if an object behaves like a type.

| ABC              | Module            | What It Represents                                   |
| ---------------- | ----------------- | ---------------------------------------------------- |
| `Iterable`       | `collections.abc` | An object that supports iteration (`for x in obj`).  |
| `Iterator`       | `collections.abc` | An `Iterable` that also implements `__next__()`.     |
| `Sequence`       | `collections.abc` | Like `list` or `tuple` (supports `len()`, indexing). |
| `Mapping`        | `collections.abc` | Like `dict` (supports key-value access).             |
| `MutableMapping` | `collections.abc` | A `dict`-like structure that can be modified.        |

```py
from collections.abc import Iterable

print(isinstance([1, 2, 3], Iterable))  # True, because a list is iterable
print(isinstance(42, Iterable))  # False, an integer is not iterable
```