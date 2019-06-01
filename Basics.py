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