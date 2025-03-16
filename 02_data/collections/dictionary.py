# mutuable
# ordered, changable, indexed, duplication not allowed

address = {
    "Flat": 91,
    "Apartment": "Sadar",
    "City": "Mayur Vihar",
    "State": "Delhi",
    "Pin_code": 110091,
    "is_current": False
}

old_address = address.copy()

# access
print(old_address["Pin_code"])
print(old_address.get("City")) # get doesn't raise error when accesing non-existing keys

# iteration
# item = key + value
for key in old_address:
    print(key, old_address[key])

for key, value in old_address.items():
    print(value)

# conditional
if "is_current" in old_address:
    print('Why did you go🥲')

# pop vs popitem
kuch_mila = old_address.pop("State")
print(old_address)
print(kuch_mila)

kuch_mila = old_address.popitem() # takes no argument
print(old_address)
print(kuch_mila)


# * (spread operator for list/tuples), ** (spread operator for dictionary); both are called unpacking operator.
new_address = {**address}
new_address["Flat"] = 68
new_address["Apartment"] = 'Parwana'
new_address["is_current"] = True 
print(new_address)

# nested dict
my_dict = {
    'one': {
        '0': 'a',
        '1': 'b',
        '2': 'c'
    },
    'two': {
        '3': 'd',
        '4': 'e'
    }
}

print(my_dict['one']['1'])

# dict comprehension
squared_odd_num = {x:x**2 for x in range(10) if x % 2 != 0}
print(squared_odd_num)

# clear
old_address.clear()
print(old_address)

# making dict from keys
keys = ['first', 'second', 'third']
default_value = None
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)