All of this works in JS and Python both.
Both languages have first class functions so stuff like closures, higher order functions are also applicable.

# Theory
- when you make a function, inside a memory (entire mem block = 'global'), a new 'home' is given to it.
- whatever is inside a home will be known and accessed inside there only regardles of if global has the same name variable in it.
- when you make a function inside a function, a new 'room' is given to it inside that 'home'.
- samilarly variable inside room won't be affected by whatever same name variable is inside the home.
- BUT in case in a home you refer to a name that only exists globally and not inside home then the value of global one will be used.
- ⭐ 'Climbing' the ladder of room -> home -> global, to find the reference of a name used inside incase the inside doesn't explicitly define the reference of it by itself.

# Example
```py
x = 99
def f1():
    x = 88
    def f2():
        print(x)
    return f2

result = f1()
result()
# Output: 88 cause the room checks in the home first if the reference for 'x' is defined
```
```py
x = 99
def f1():
    def f2():
        print(x)
    return f2

result = f1()
result()
# Output: 99 cause the room checks in the home, doesn't find it, so then checks in global for reference of 'x'
```
- closure: the inner function doesn't just have the defination/declaration but also all the references of variables and parameters used by the outer function (backpack/tiffin concept).
- in python closure are also called factory function.

```py
def f1(num):
    def f2(x):
        return x ** num
    return f2

a = f1(3)
b = f1(2)
result1 = a(3)
result2 = b(3)
print(result1)
# Output: 27 -> 3 ** 3
print(result2)
# Output: 9 -> 3 ** 2
```