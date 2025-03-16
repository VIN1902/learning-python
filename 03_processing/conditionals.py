# 1.

user_age = input('Enter your age: ')
user_age = int(user_age)
if user_age < 13:
    print('child')
elif user_age < 20:
    print('teenager')
elif user_age < 60:
    print('adult')
else:
    print('senior')

# 2. ternary 

movie_price = 12 if user_age >= 18 else 8
day = input('what day is it? ')
if day == 'wednesday':
    movie_price -= 2

print("You are {} year old and as today is {}, your movie ticket will cost ${}.".format(user_age,day,movie_price))

# break -> exit out of loop scope
# continue -> skip that iteration of loop
# return -> exit out of function scope
# exit() -> exit out of program/script

# 3.

year = input('What year is it? ')
year = int(year)
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print('{} is a leap year'.format(year))
else:
    print('{} is not a leap year'.format(year))

# 4. match case (switch)

weather = input('How\'s the weather today? ')
match weather:
    case 'Sunny':
        print('Go outside')
    case 'Rainy':
        print('Take an umbrella')
    case 'Snowy':
        print('Build a snowman')

# Unlike switch-case in C/C++, Python's match statement does not fall through (i.e., once a case matches, no other cases are checked).