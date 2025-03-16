# immutable
# ordered, unchangable, indexed, duplication allowed

# so literally lists but immutable

my_tuple = (1,2,3,4)
# access
my_tuple[1]
my_tuple[-1]

# slice
my_tuple[1:]

# concatination (also there in list)
her_tuple = ('makeup', 33, False)
our_tuple = my_tuple + her_tuple
print(our_tuple)

# conditional (for checking existence)
if 'makeup' in our_tuple:
    print('okay')

# tuple destructuring (unpacking)
(carrying, age, is_real) = her_tuple
sentence = "She is {} years old and carrying {} with her, but is she real? {}"
print(sentence.format(age,carrying,is_real))

# len and type (is there for other collections too)
len(our_tuple)
type(our_tuple)

# nested tuple also exists