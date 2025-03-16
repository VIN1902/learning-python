my_str = "Vikas Indora"
my_str[0]
my_str[-1] # negative indexing allowed even for accessing

# slice (.slice() in js)
my_str_slice = my_str[0:2]
print(my_str_slice)
my_str[:]
my_str[:4]
my_str[1:]
my_str[0::2] # 3rd argument is 'hop' also non-inclusive like 2nd argument

# case (.toUpperCase() in js)
my_str.lower()
my_str.upper()
my_str.title()
my_str.capitalize()

# strip (.trim() in js)
my_str.strip()
# lstrip() == trimStart(), rstrip() == trimEnd()

# replace (.replace() in js)
my_str.replace("Vikas", "Virender")

# split (.split() in js)
my_str.split(" ") # same as defualt sperator .split()

# find (.indexOf() in js)
my_str.find("Indora") # returns -1 if not found

# count 
my_str.count('a')

# string interpolation
sentence = "My name is {}!"
print(sentence.format(my_str))

# join (.join() in js; for py: just switch array and seperator)
list = ['u','r','m','i','l','a']
"".join(list)

# len (length() in js; for py: just don't call it, instead use a global method for any string)
len(my_str)

# escape character
sentence = "He said \"go out!\" in front of everyone"
print(sentence)
path = r"C:\\Desktop\my_folder" # raw string => ignore escape character
print(path)

# string containing question
print('He' in sentence)