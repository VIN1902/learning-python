# mutable
# ordered, changeable, indexed, duplication allowed

my_list = ['Spiderman', 'Flash', 'Batman', 'Wolverine']

# access, negative
print(my_list[-1])
my_list[len(my_list)-1] = 'Superman'
print(my_list)

# slice
print(my_list[:2])

# splice() mimic from js
my_list[1:3] = ['Thor','Hawkeye'] # splice(1,2,'','')
print(my_list) 
my_list[1:1] = ['Hulk'] # splice(1,0,'')
print(my_list)
my_list[1:2] = [] # splice(1,1)
print(my_list)

# membership testing ('in' operator)
if 'Spiderman' in my_list:
    print('Best Superhero')

# iteration
for hero in my_list:
    if hero == my_list[-1]:
        print(hero)
    else:
        print(hero, end='-')

# golden array methods
my_list.append('Ironman') # .push() in js
my_list.pop() # .pop() in js
my_list.insert(0, 'Ironman') # .unshift() in js
my_list.pop(0) # .shift() in js

print(my_list.pop(1))
print(my_list)

# copy
new_list = my_list.copy() # same as [...my_list] in js
new_list.append('Iamcopy')
print(my_list)
print(new_list)

# list comprehension (inplace of map and filter from js) -> lets you to generate list dynamically
squared_list = [x**2 for x in range(10)]
print(squared_list)
even_list = [x for x in range(10) if x % 2 == 0]
print(even_list)