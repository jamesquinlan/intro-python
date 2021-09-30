# - Introduction to Programming with Python
# - Chapter 2 Exercises on IF statements
# - DSC-225 Fall 2021
# - Quinlan, J


# 2.1
"""
Create the statements ```x=2``` and ```y=3```, then determine what each of 
what each of the following displays.
"""

x=2
y=3

print('x = ',x)                           # a.
print('Value of',x,'+',x,'is',(x+x))      # b.
print('x=')                               # c
print((x+y),'=',(y+x))                    # d.
# ----------------------- #

# 2.2 (What's wrong with this code?) 
""" 
The following code should read an integer in the variable `rating`.
"""
rating = input('Enter an integer rating between 1 and 10: ')

# Answer: There are no runtime errors, however, there are logical errors. 
# In particular, there is nothing that prevents the user from entering 345 or 
# a string like, 'The cool cat cooks for criminals'.
# ----------------------- #



# 2.3 (Fill in the missing code by replacing ***).  See page 71.  
""" 
The code below is the correct code after filling in missing ***.
"""

grade = 95
if grade >= 90:
  print('Congratulations! Your grade of', grade, 'earns you an A in this course.')

# ----------------------- #



# 2.4 (Arithmetic) 

print('27.5 + 2 = ', 27.5 + 2)      # Addition
print('27.5 - 2 = ', 27.5 - 2)      # Subtraction
print('27.5 * 2 = ', 27.5 * 2)      # Multiplication
print('27.5 / 2 = ', 27.5 / 2)      # Division
print('27.5 // 2 = ', 27.5 // 2)    # Floor Division
print('27.5 ** 2 =', 27.5 ** 2)     # Exponentiation

# ----------------------- #




# 2.5 (Circle area, Diameter, and Circumference) 
"""
For a circle of radius 2, display the diameter, circumference, and area.  
Use the value 3.14159 for \pi.  # NOTE: Python's math module provides a high 
precision representation for pi.
"""

pi = 3.14159
r = 2

area = pi*(r**2)  # are the () necessary?
diameter = 2*r
circumference = 2*pi*r

print('Area = ',area, ', ','Diameter = ', diameter, ', ' 'Circumference = ', circumference)

# ----------------------- #



# 2.6 (odd or even) 
"""
Use if statements to determine whether an integer is even or odd.
# Hint: Use the remainder operator (modular arithmetic)
"""

x = 53432
if x % 2 == 0:
  print('Even')
else:
  print('Odd')

# ----------------------- #



# 2.7 (Multiples) 
"""
Use if statements to determine whether 1024 is a multiple of 4 and whether 2 
is a multiple of 10.
"""

if 1024 % 4 == 0:
  print('1024 is a multiple of 4')
else:
  print('1024 is NOT a multiple of 4')

if 2 % 10 == 0:
  print('2 is a multiple of 10')
else:
  print('2 is NOT a multiple of 10')

# ----------------------- #



# 2.8 (Tables of Squares & Cubes)
""" 
Write a script that calculates the squares
and cubes of the numbers from 0 to 5.  Print the resulting values in table
format.  Use the tab escape sequence to achieve the three-column output 
"""

print('number \t square \t cube')
print(0,'\t',0,'\t', 0)

# ----------------------- #



# 2.9 (Integer Value of a Character)
"""
Each of a string's characters has an integer representation.  The set of characters
with the integer representation is called a __character set__.  A character is
indicated with single quotes, e.g., 'A'.  To determine a character's integer
value, use the built-in function ORD to display values for: BCDbcd012$*+
"""

B=ord('B');print('B = ',B)
C=ord('C');print('C = ',C)
D=ord('D');print('D = ',D)
b=ord('b');print('b = ',b)
c=ord('c');print('c = ',c)
d=ord('d');print('d = ',d)
u=ord('0');print('0 = ',u)
v=ord('1');print('1 = ',v)
w=ord('2');print('2 = ',w)
x=ord('$');print('$ = ',x)
y=ord('*');print('* = ',y)
z=ord('+');print('+ = ',z)

# ----------------------- #



# 2.10 (Arithmetic, Smallest, and Largest)
"""
Write code that inputs three integers from the user.  Display the sum, average, 
product, smallest, and largest of the inputs.  
"""

x = int(input('Enter first integer: '))
y = int(input('Enter second integer: '))
z = int(input('Enter third integer: '))

print(x+y+z)
print((x+y+z)/3)
print(x*y*z)
print(min(x,y,z))
print(max(x,y,z))

# ----------------------- #



# 2.11 (Separating the digits in an integer)
"""
Write code that inputs a five-digit integer.  Separate the number into digits.
Print them separated by three spaces each.  For example, 42339 would be printed
4   2   3   3   9
Assume user enters correct number of digits (no leading zeros).  Use FLOOR and
REM to isolate the digits.  
"""

digits = [0, 0, 0, 0, 0]

# x=42339
x=int(input('Enter a 5 digit integer'))
digits[4] = x % 10

x = x//10
digits[3] = x % 10

x = x//10
digits[2] = x % 10

x = x//10
digits[1] = x % 10

x = x//10
digits[0] = x % 10


print(digits[0],'   ',digits[1],'   ',digits[2],'   ',digits[3],'   ',digits[4])

# ----------------------- #




# 2.12 (7% Investment Return)
"""
Let P = $1000.  Calculate and display how much money after 10, 20, and 30 years
using the formula A = P(1+r)^n where r = 7% and n = 10, 20, 30.  A is the amount
of deposit at the end of the nth year.  
"""

P = 1000
r = 0.07

# 10 years
n = 10
A = round(P*(1+r)**n,2)
print(A)

# 20 years
n = 20
A = round(P*(1+r)**n,2)
print(A)


# 30 years
n = 30
A = round(P*(1+r)**n,2)
print(A)

# ----------------------- #







# 2.13 (How big can Python integers be?)
"""
Experiment with 2**X for large numbers X.  See if you can break it.
Make note of the time it takes to compute.  
"""

X = 3453454
print(2**X)

# 2.14 (Target Heart-rate Calculator)
"""
Your target heart rate is 50 - 85% of your maximum heart rate in beats per minute.  
The formula to caluate a persons maximum heart rate (according to the American 
Heart Association, AHA) is: 220 - Age (in years).

Write code to prompt user for age, then calculate maximum heart rate and target
range.  
"""

Age = int(input('Enter your age (in years): '))
MaxHeartRate = 220 - Age
Target = [round(0.5*MaxHeartRate,0), round(0.85*MaxHeartRate,0)]
print('Your Max Heart Rate is: ', MaxHeartRate)
print('Your Target range is: ', Target)

# ----------------------- #





# 2.15 (Sort in Ascending Order)
"""
Write code that inputs three different floating-point numbers from the user.  
Display the numbers in increasing order.  Test using all 6 possible orders.
Does your script work with duplicate numbers?
"""

# Obtain input from user
#x = input('First number = ')
#y = input('Second number = ')
#z = input('Third number = ')

x = 3
y = 3
z = 1

if x < y and x < z:
  one = x
  if y < z:
    two = y
    three = z
  else:
    two = z
    three = y
elif y < x and y < z:
  one = y
  if x < z:
    two = x
    three = z
  else:
    two = z
    three = x
else:
  one = z
  if x < y:
    two = x
    three = y
  else:
    two = y
    three = x
  

print(one, two, three)

# ----------------------- #