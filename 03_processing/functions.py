# 1. syntax
def power_of_number(number,power):
    return number ** power

result = power_of_number(4,5)
print(result)

# 2. polymorphism
def multiply(num1, num2):
    return num1 * num2
string_multiplication = multiply('V', 5)
number_multiplication = multiply(5, 5)
print(string_multiplication)
print(number_multiplication)

# 3. return multiple values
import math
def circle_stat(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * (radius * radius)
    return circumference, area

circle_tuple = circle_stat(6)
print(circle_tuple)
circle_area, circle_circumference = circle_stat(4)
print('Area: {}, Circumference: {}'.format(round(circle_area, 2), round(circle_circumference, 2)))

# Handling precision:
# in JS number.toFixed(decimal) is same as round(number, decimal) in Python.
# in JS Math.round(number) returns the nearest integer.

# 4. default parameter
def greet(name = 'Eren'):
    return 'Hello {}!'.format(name)

print(greet())

# 5. lambda function ; arrow or function expression in JS
cube_of_number = lambda num: num ** 3
print(cube_of_number(2))

# 6. *args (only the '*' is keyword, 'args' is a tuple)
def spread1(*args):
    for i in args:
        print(i)
spread1(1,2,3,4,5,6)

ye_rhi_list = [6,7,8,9,10]
spread_in_other_list = [*ye_rhi_list, 11, 12 ,13, 14,15]
print(spread_in_other_list)

# * expands the iterable. (similar to using ... outside a function in JS)
# * (*args) also collects multiple arguments in a tuple, when used as a function parameter. (similar to using ... inside a function parameter in JS)

# ** expands key:value items in a dict.
# ** (**kwargs) also collects mutliple arguments in key:value fashion inside a dict, when used as a function parameter.

# 7. **kwargs
def spread2(**kwargs):
    for key, value in kwargs.items():
        print('{}: {}'.format(key,value))
spread2(name='sakiv', age=15)

ye_rhi_dict = {'name': 'vikas', 'age': 22}
spread_in_other_dict = {**ye_rhi_dict, 'is_frustrated_with_python': True}
print(spread_in_other_dict)

# 8. function with yield
def even_generator(limit):
    gen_list = [i for i in range(1, limit + 1) if i % 2 == 0]
    return gen_list
print(even_generator(10))

# but we don't want a list
# yield = similar to return; freeze the execution and return the value to caller, now on next call state is retained of execution.

def even_yield(limit):
    for i in range(2, limit + 1, 2):
        yield i

for thing in even_yield(20):
    print(thing)

# in js terms yield unlike return, does not end the execution context but pauses it and returns current value to caller. Then resumes when next value is called.
# using yield keyword ensures that the return of function (called a generator) is always an iterable. and that has a method called .next(), which moves the generator to the next yield statement.
'''
function* myGenerator() {
    yield "Hello";
    yield "World";
    return "Done";  // Final return value
}

const gen = myGenerator();

console.log(gen.next()); // { value: "Hello", done: false }
console.log(gen.next()); // { value: "World", done: false }
console.log(gen.next()); // { value: "Done", done: true }
console.log(gen.next()); // { value: undefined, done: true }
'''

# uder the hood of for-of loop (in python):
'''
gen = even_yield(20)
print(next(gen)) # 2
print(next(gen)) # 4
print(next(gen)) # 6
print(next(gen)) # 8
...and so on
'''

'''
Key difference between JS and Python's next method on a generator
- In js next returns an object with keys value and done, at the end done is set to true. works with generator only.
- In python next returns just the value, at the end it raises an error. (stopIteration exception) works with any iterable and not just with generators, cause that's how the lang is designed.
'''

# 9. recursive function for factorial
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
print(factorial(5))
# in recursions the main thing to focus on is exit statement