a=5
b=6
c=a+b
print(c)
print("Hello world")
raw_str='Blue\nRed\nGreen'
print(raw_str)
style_char='*'
style_char*10
poem="""\
Different world
Youdian tian
"""
print(poem, end='')
he='buffalo'
print(he*10)
string1='hello'
mess=f'{string1} there'
print(mess)
a=9%5
print(a)
def greeting():
    print("-----------------------------")
    print("         Hello World         ")
    print("-----------------------------")
greeting()

def sum_two_numbers(num1, num2):
    total = num1 + num2
    print("{} + {} = {}".format(num1, num2, total))
sum_two_numbers(3, 4)

def num_square(num):
    return num * num
my_num = 3
print(num_square(2))
print(num_square(my_num))

def greeting(style_char='-'):
    print(style_char * 29)
    print(" Hello World ")
    print(style_char * 29)

greeting()

mystr = "Hello World\nHello Python"
print (mystr)

print("hi", end='-??\n')

a=8
b=5
print(a+b, a-b, sep=':')

raw_str = r'Blue\nRed\nGreen'
print(raw_str)

poem = """\
The woods are lovely, dark and deep,
But I have promises to keep,
And miles to go before I sleep,
And miles to go before I sleep.
"""
print(poem, end='')

amount =  15
print("We have " + str(amount) + " tables in our lab")

num1 = 42
num2 = 7
print('{0} + {1} * {0} = {2}'.format(num1, num2, num1 + num2 * num1))

appx_pi = 22 / 7
print("{0:>10.3f} and 5.12".format(appx_pi))

print('Binary value of 42 = {:b}'.format(42))

print('Binary value of 42 = {:#b}'.format(42))

num1 = 42
num2 = 7
print(f'{num1} + {num2} = {num1 + num2}')

raw_str = 'Blue\nRed\nGreen'
print(raw_str)

range(5)

list(range(5))

type(5)

def print_num():
    print("Yeehaw! num is visible in this scope, its value is: " + str(num))
num = 25
print_num()

def square_of_num(num):
    square_of_num = num * num
square_of_num(5)
print("5 * 5 = {}".format(square_of_num))

sqr_num = 4
def square_of_num(num):
    sqr_num = num * num
    print("5 * 5 = {}".format(sqr_num))
square_of_num(5)
print("Whoops! sqr_num is still {}!".format(sqr_num))

def square_of_num(num):
    sqr_num = num * num
    print("5 * 5 = {}".format(sqr_num))
square_of_num(3)

usr_ip = "12"
usr_num = int(usr_ip)
sqr_num = usr_num * usr_num
print("{}".format(sqr_num))

usr_ip = "23.23"
usr_num = float(usr_ip)
sqr_num = usr_num * usr_num
print("Square of entered number is: {0:.2f}".format(sqr_num))

usr_name = "Hi there! What's your name? "
usr_color = "And your favorite color is? "
print("{}, I like the {} color too".format(usr_name, usr_color))

import subprocess
subprocess.call('date')
print("\nToday is ", end="", flush=True)

fav_fiction = 'Harry Potter'
fav_detective = 'Sherlock Holmes'
fav_fiction == fav_detective

if -1:
    print("-1 evaluates to True in condition checking")

def num_chk(n):
    if n == 10 or n == 21 or n == 33:
        print("Number passes condition")
    else:
        print("Number fails condition")
num_chk(10)
num_chk(12)

def num_chk(n):
    if n in (10, 21, 33):
        print("Number passes condition")
    else:
        print("Number fails condition")
num_chk(12)
num_chk(10)

num = 45
if num > 25:
    print("Hurray! {} is greater than 25".format(num))

num = 45
if num % 2 == 0:
    print("{} is an even number".format(num))
else:
    print("{} is an odd number".format(num))

num = 0
if num < 0:
    print("{} is a negative number".format(num))
elif num > 0:
    print("{} is a positive number".format(num))
else:
    print("{} is neither postive nor a negative number".format(num))

num = 42
num_type = 'even' if num % 2 == 0 else 'odd'
print("{} is an {} number".format(num, num_type))

num1 = 35
num2 = 42
comparison = "greater" if (num1 - num2) > 0 else "smaller"
print("{} is {} than {}".format(num1, comparison, num2))

number = 9
for i in range(2, 4):
    mul_table = number * i
    print("{} * {} = {}".format(number, i, mul_table))

usr_string = 'not a number'
while not usr_string.isnumeric():
    usr_string = input("Enter a positive integer: ")

prev_num = 0
curr_num = 0
print("The first ten numbers in fibonacci sequence: ", end='')
for num in range(10):
    print(curr_num, end=' ')
    if num == 0:
        curr_num = 1
        continue
    temp = curr_num
    curr_num = curr_num + prev_num
    prev_num = temp
print("")

import random
while True:
    random_int = random.randrange(500)
    if random_int % 4 == 0 and random_int % 6 == 0:
        break
print("Random number divisible by 4 and 6: {}".format(random_int))

while True:
    usr_string = input("Enter a positive integer: ")
    if usr_string.isnumeric():
        break

string = '123456'
print(string.isnumeric())

vowels = ['a', 'e', 'i', 'o', 'u']
vowels[0]

even_numbers = list(range(2, 11, 2))
even_numbers[-1]
even_numbers[-2]

student = ['learnbyexample', 2016, 'Linux, Vim, Python']
print(student)

list_2D = [[1, 3, 2, 10], [1.2, -0.2, 0, 2]]
list_2D[0]

prime = [2, 3, 5, 7, 11]
prime[3:1:-1]

numbers = [2, 12, 3, 25, 624, 21, 5, 9, 12]
odd_numbers = []
even_numbers = []
for num in numbers:
    odd_numbers.append(num) if (num % 2) else even_numbers.append(num)
print("numbers: {}".format(numbers))
print("odd_numbers: {}".format(odd_numbers))
print("even_numbers: {}".format(even_numbers))

north_dishes = ['Aloo tikki', 'Baati', 'Khichdi', 'Makki roti', 'Poha']
print("My favorite North Indian dishes:")
for idx, item in enumerate(north_dishes):
    print("{}. {}".format(idx + 1, item))

north_dishes = ['Aloo tikki', 'Baati', 'Khichdi', 'Makki roti', 'Poha']
for idx, item in enumerate(north_dishes, start=1):
    print(idx, item, sep='. ')

odd = [1, 3, 5]
even = [2, 4, 6]
for i, j in zip(odd, even):
    print(i + j)

import time

numbers = list(range(1,100001))
fl_square_numbers = []
t0 = time.perf_counter()
for num in numbers:
    fl_square_numbers.append(num * num)
t1 = time.perf_counter()
lc_square_numbers = [num * num for num in numbers]

t2 = time.perf_counter()
fl_time = t1 - t0
lc_time = t2 - t1
improvement = (fl_time - lc_time) / fl_time * 100

print("Time with for loop:           {:.4f}".format(fl_time))
print("Time with list comprehension: {:.4f}".format(lc_time))
print("Improvement:                  {:.2f}%".format(improvement))

if fl_square_numbers == lc_square_numbers:
    print("\nfl_square_numbers and lc_square_numbers are equivalent")
else:
    print("\nfl_square_numbers and lc_square_numbers are NOT equivalent")
    
numbers = [2, 12, 3, 25, 624, 21, 5, 9, 12]
odd_numbers = []
even_numbers = []
[odd_numbers.append(num) if(num % 2) else even_numbers.append(num) for num in numbers]

numbers = [2, 12, 3, 25, 624, 21, 5, 9, 12]
odd_numbers = [num for num in numbers if num % 2]
even_numbers = [num for num in numbers if not num % 2]

p = [1, 3, 5]
q = [3, 214, 53]
[i+j for i,j in zip(p, q)]
[i*j for i,j in zip(p, q)]
sum(i*j for i,j in zip(p, q))

book = "Alchemist"
book[0]

import string
string.ascii_uppercase[:10]
list(string.digits)

nums = [3, 2, 5, 7, 1, 6.3]
len(nums)

book
'Alchemist'
set(book)

nums = {1, 2, 3, 5, 6.3, 7}
nums.pop()
nums

language = ['Python', 'Java', 'C++', 'Ruby', 'C']
language.pop(-3)
language
print('When index is not passed:')
print('Return Value: ', language.pop(-3))

nums = {1, 2, 3, 5, 6.3, 7}
for n in nums:
    print(n)


fav_books = {}
fav_books['fantasy'] = 'Harry Potter'
fav_books['detective'] = 'Sherlock Holmes'
fav_books['thriller'] = 'The Da Vinci Code'
fav_books

for book in fav_books.values():
    print(book)

a = {"a":2,"b": 5, "c":3}
a.keys()
for thing in a.keys():
    print(thing)

marks = {'Rahul' : 86, 'Ravi' : 92, 'Rohit' : 75}
marks.values()
marks.items()
for a, b in marks.items():
    print(a, b, sep=": ")

fav_books = {'thriller': 'The Da Vinci Code', 'fantasy': 'Harry Potter', 'detective': 'Sherlock Holmes'}
import pprint
pp = pprint.PrettyPrinter(indent=1)
pp.pprint(fav_books)

import random
north = ['aloo tikki', 'baati', 'khichdi', 'makki roti', 'poha']
south = ['appam', 'bisibele bath', 'dosa', 'koottu', 'sevai']
west = ['dhokla', 'khakhra', 'modak', 'shiro', 'vada pav']
east = ['hando guri', 'litti', 'momo', 'rosgulla', 'shondesh']
dishes = {'North': north, 'South': south, 'West': west, 'East': east}
random.choice(dishes['South'])

rand_zone = random.choice(tuple(dishes.keys()))
rand_dish = random.choice(dishes[rand_zone])
print("Try the '{}' speciality '{}' today".format(rand_zone, rand_dish))

marks = {'Rahul' : 86, 'Ravi' : 92, 'Rohit' : 75, 'Rajan': 79}
for nam, mark in marks.items():
    print(f'{nam:5s}: {mark}')

greeting = '===== Have a great day!! ====='
greeting.translate(str.maketrans("!", "y", "H"))

import string
quote = 'SIMPLICITY IS THE ULTIMATE SOPHISTICATION'
tr_table = str.maketrans(string.ascii_uppercase, string.ascii_lowercase)
quote.translate(tr_table)

greeting = ' Have a nice day :) '
greeting.strip(": )")

' Hello World '.center(40, '*')

'abc'.isnumeric()

sentence = 'This is a sample string'
sentence.count('s')

"oranges:5".split('g')

import re
string = "This is a sample string"
bool(re.search('this', string))

string = "This is a sample string"
re.findall('is', string)

string = "This is a sample string"
re.findall('\w+', string)

import re
quote = "So many books, so little time"
re.search(r'([a-z]{2,}).*\1', quote, re.I)

import re
greeting = '***** Have a great day *****'
re.sub('*', '=', greeting)

import re
xx = "guru99,education is fun"
r1 = re.findall(r"^\w+",xx)
print(r1)

