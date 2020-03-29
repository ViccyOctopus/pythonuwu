while <condition>:
    <expression>
    <expression>
    ...

n = input("You are in the Lost Forest. Go left or right? ")
while n == "right":
    n = input("You are in the Lost Forest. Go left or right? ")
print("you got out of the Lost Forest!")

n = 0
while(n < 5):
    print(n)
    n = n + 1

Output: 0, 1, 2, 3, 4

for n in range(5):
    print(n)

Output: 0, 1, 2, 3, 4

mysum = 0
for i in range (7, 10):
    mysum += i
print(mysum)

mysum = 0
for i in range(5, 11, 2):
    mysum += i
print(mysum)

mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
print(mysum)

x=3
ans = 0
itersLeft = x
while (itersLeft != 0):
    ans = ans + x
    itersLeft = itersLeft - 1
print(str(x) + "*" + str(x) + "=" + str(ans))

#This code squares the value of x by repietitive additon

x = int(input("Enter an integer: "))
ans = 0
while ans**3 < x:
    ans += 1
if ans**3 != x:
    print(str(x) + 'is not a perfect cube')
else:
    print("Cube root of " + str(x) + " is " + str(ans))


x = int(input("Enter an integer: "))
ans = 0
while ans**3 <abs(x):
    ans += 1
if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = - ans
    print('Cube rot of ' + str(x) + ' is ' + str(ans))

cube = 8
for guess in range(cube + 1):
    if guess**3 == cube:
        print("Cube root of", cube, "is", guess.)



ans = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag = True
while ans**2 < x:
    ans += 1
if ans**2 == x:
    print("Square root of", x, "is", ans)
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print("Just checking... did you mean", -x, "?")


s = "abc"

len(s) #evaluates to 3
s[0]   #evaluates to "a"
s[1]   #evaluates to "b"
s[2]   #evaluates to "c"
s[3]   #trying to index out of bounds, error

s = "abcdefgh"
s[::-1] -> evaluates to "hgfedcba"
s[3:6]  -> evaluates to "def"
s[-1]   -> evaluates to "h"

#strings are imumutable, meaning they cannot be modified
s = "hello"
s[0] = "y"  -> gives an error
s = "y" + s[1:]
#where the output is yellow


s = "abcdefgh"
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("There is an i or u")

for char in s:
    if char == 'i' or char == 'u':
        print("There is an i or u")


cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print("Failed on cube root of", cube)
else:
    print(guess, 'is close to the cube root of', cube)


x = 25
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) > epsilon:
    print('low = ' + str(low) + 'high = ' + str(high) + "ans = " + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + 'is close to square root of ' + str(x))


if num < 0:
    isNeg = True
    num = abs(num)
else:
    is Neg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2
if isNeg:
    result = '-' + result


def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ", " + firstName)
    else:
        print(firstName, Lastname)

printName('Victoria','Arzumanova', False)


def mult_iter(a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

#Multiply a*b, which is the same as adding a to itself b times
#It subtracts b once, then adds a, subtracts b once, adds a
#Suppose you want to do 5 times 3
#b: 5 4 3 2  1  0
#a: 3 6 9 12 15


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

#the file circle.py contains
pi = 3.14159
def area(radius):
    return pi*(radius**2)
def circumference(radius):
    return 2*pi*(radius)

import circle
pi = 3
print(pi)
print(circle.pi)
print(circle.area(3))
print(circle.circumference(3))

This gives you:

3
3.14149
28.27431
18.84953999999998

from circle import *
print(pi)
print(area(3))