# best practices:
float(40) + 22.69
(3 + 4) * 7
'vikas' + 'indora' # operator overloading

x = 1
y = 2
z = 3
what = x, y, z # tuple output
print(what)

x < y and y < z # same as x < y < z, cause of chained comparison
x < y or y > z
1 == 2 < 3 # same as (1 == 2) and (2 < 3)

# math module
import math
math.floor(3.4)
math.floor(-3.4)
math.trunc(-3.4)
math.ceil(3.8)
math.ceil(-3.8)

# base
binary = 0b111
octal = 0o20
hexa = 0xff

binary = bin(7)
octal = oct(16)
hexa = hex(255)

binary = int('7', 2)
octal = int('16', 8)
hexa = int('255', 16)

# bitwise operator
1 << 2 # left-shift '1' (decimal converted to binary) by '2' bits
8 >> 3 # right-shift '8' (decimal converted to binary) by '3' bits

1 | 2 # bitwise OR
1 & 2 # bitwise AND

# random module
import random
random.random() # b/w 0 and 1 (float)
random.randint(1,6) # b/w 1 and 6 (both included)
l1 = ['apple', 'mango', 'banana']
random.choice(l1)
random.shuffle(l1)

# handle floating point numbers
from decimal import Decimal
Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.2')

# bool
type(True)
print(True == 1) # True
print(False == 0) # True
print(True is 1) # False