# break -> exit out of loop scope
# continue -> skip that iteration of loop
# return -> exit out of function scope
# exit() -> exit out of program/script

# 1. count +ve numbers from a list

numbers = [1,2,-1,3,4,-2,5,6,-3,-4]
positive_number_count = 0
for num in numbers:
    if num >= 0:
        positive_number_count += 1

print('{} this list of length {}, has {} positive elements'.format(numbers, len(numbers), positive_number_count))

# 2. sum of even numbers upto n number

random_number = 10
sum_of_even_num = 0
for n in range(1, random_number + 1):
    if n % 2 == 0:
        sum_of_even_num += n
print('Sum of even number form-1-to-{} is {}'.format(random_number, sum_of_even_num))

# 3. print table skip random entry

tabe_of = 6
for i in range(1,11):
    if i == 5:
        continue
    print('{} X {} = {}'.format(tabe_of,i,tabe_of*i))

# 4. reverse a string

string_to_reverse = 'vikas'
reversed_string = ''
for letter in string_to_reverse:
    reversed_string = letter + reversed_string
print(reversed_string)

# 5. find first non-repeating character

string_with_repeating_char = 'teeter'
for char in string_with_repeating_char:
    if string_with_repeating_char.count(char) == 1:
        print(char)
        break

# 6. while loop factorial

factorial_of = 5
factorial_ans = 1
while factorial_of > 0:
    factorial_ans *= factorial_of
    factorial_of -= 1
print(factorial_ans)

# 7. keep asking for input until they enter something between 1 and 10

while True:
    input_question = int(input('Enter a value b/w 1 and 10: '))
    if input_question > 0 and input_question < 11:
        print('Your number is', input_question)
        break

# 8. prime checker

prime_number = 13
for i in range(2,10):
    if prime_number == 1:
        print('{} is prime'.format(prime_number))
        break
    elif prime_number % i != 0 and prime_number != i:
        print('{} is prime'.format(prime_number))
        break
    else:
        print('{} is not prime'.format(prime_number))
        break

# 9. find list duplicate

duplicate_list = ['apple', 'orange', 'apple', 'banana', 'grape']
for fruit in duplicate_list:
    if duplicate_list.count(fruit) > 1:
        print('{} is duplicate in given list'.format(fruit))
        break

unique_bucket = set()
for fruit in duplicate_list:
    if fruit in unique_bucket:
        print("Duplicate:",fruit)
        break
    unique_bucket.add(fruit)

