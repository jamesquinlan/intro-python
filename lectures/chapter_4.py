# Functions

Functions are essential to the __divide and conquer__ paradigm of problem solving and faciliate program management as the program can be broken into manageable pieces.  

## Lesson Objectives

*   Define user functions
*   Import python libraries
*   Pass data betweeen functions
*   Gengerate random numbers
*   Perform simulations (using random numbers)
*   Pack and upack from tuples
*   Return multiple values from function
*   Identify __scope__ of variables


---

## Defining Functions

There are many built-in functions (e.g., `sum`, `len`, `min`, `mean`).  Each function should __perform a single, well-defined task__.  Custom functions, (a.k.a. user-defined functions) can be defined as needed.  

A __function definition__ begins with the ```def``` _keyword_, followed by the name of the function, a set of input values separated by commas enclosed in parenthesis and then a colon.  A __docstring__ should be included and a ```return``` statement which passes control back to the caller with the computed output value of the function.  
```
def function_name(inputs):
  '''Docstring'''
  return output  
```

A simple example of a function that squares the input value.
"""

def square(number):
  """Square a number"""
  return number**2

"""A function is callled (invoked) as such:"""

square(6)

"""View the docstring and function information."""

import os
os.open?

square?

"""---

A function is analogous to the concept of __mathematical function__.  In particular, suppose $f(x) = x^2-5x+6$.  In python, we can create this function using the code below.
"""

def f(x):
  """f(x) = x^2 -5x + 6"""
  return x**2 - 5*x + 6

"""And evaluate it at say, 2
 (at 2)
"""

f(2.3454534)

"""Or 5"""

f(6)

"""A function without a ```return``` statement implicitly returns ```None``` (see Table on page 77) keyword. Use ```pass``` instead of ```return``` when first building a function (before the inner code block is developed), such as a function template or function placeholder."""

def f(x):
  """Does nothing"""
  return None

def g(x):
  return

def h(x):
  """Skips this function.  Does not return None"""
  pass

# Call functions g and h
print(g(3))
h(2)

"""## Passing by Reference or by Value
Python passes all arguments __by reference__.
"""

y = 4
id(y)

x = 7
print('Memory Location of x = ',id(x))
f(x)
print(x)
print('Memory Location of x = ',id(x))

def f(x):
  print('Mem. Loc. of x in f(x) = ',id(x))
  x += 1
  print(x)
  print('Mem. Loc. of NEW x, x+1, in f(x) = ',id(x))
  return None

"""## Default Parameters

When defining a function, __default parameter values__ can be specified in the arguments list.  
"""

def area_of_circle(r = 1):
  return 3.1415*r**2

# Determine the area of unit circle
area_of_circle()  # same as area_of_circle(1)

"""# Multiple Parameters
Functions can accept any number of input parameters.  
"""

def f(x,y):
  return x*y

# Call the function 
f(4,9)

def f(a,b,c):
  return a+b+c

# Call function 
f(1,2,3)

def f():
  return "No value"

# Call function 
f()

"""## Arbitrary Number of Parameters

It is sometimes desirable that a function accepts a variable number of input parameters.  For example, the ```max``` function can take two or more input values.  In particular, 

```
max(7,3)
max(3,1,8,4,9,2)
```

### ```*args```

Use ```*args``` in the function to accept a variable number of input parameters.
"""

max(7,3,1,9,10,123,456)

# Define an average function that accepts variable number of input arguments.
def avg(*args):
  return sum(args) / len(args)


# Test the function
avg(2,7,3,5,3,12,18)



"""## Local Variables

When a function is called, an identifier for the input parameter is created (temporarily) to store that value in memory for use in the body of the function.  It is then destroyed as the function passes control back to the caller.  The same applies to variables created (and used) within the function code block.  Any such identifiers are known as a __local variables__.

Attempting to access this identifier after control has return to the caller with result in a ```NameError```.  For example, 
"""

def f(x):
  y = 3*x
  print(x)
  print(id(x))
  return y

"""Lets test an input parameter.  Note, first clear any residual values of `x` in scope (in current namespace). """

# "Main" program
del x
print(f(4))
print(x)

"""Now test `y`."""

print(f(3))
print(y)

"""## Multiple input parameters

Functions can take multiple input paramenters.
"""

def maximum(x,y,z):
  """Return the maximum of three values"""
  max_ = x
  if y > max_:
    max_ = y
  if z > max_:
    max_ = z
  
  return max_

"""Call the maximum function."""

maximum(4, 1.35, 9)

"""> Note the output of ```maximum``` when  strings are the inputs."""

maximum('blue', 'red', 'green')

"""What about mixed types? """

maximum(3, 'blue', 1,, 'brown')

"""---

## Random-number Generation

Simulation is an important tool in computational science.  It relies on random generation of large sample of numbers.  The `random` module is included in the Python Standard Library. 


Simulate rolling a six-sided die 10-times.

First import the `random` module.
"""

import random

"""Roll 10 times, each time selecting a random integer between 1 and 6."""

for i in range(10):
  print(random.randint(1,6), end=' ')

"""#### Simulation Project
What about a more realistic simulation of rolling the die 100000 times?  Write a function that accepts an arbitrary positive integer to simulate rolling a fair, six-sided die that number of times keeping track of the frequency of each face.  Print a table of the results.
"""

import random

# Function defintion
def roll(n):
  """Simulating rolling 6-sided die n-times"""

  frequencies = [0, 0, 0, 0, 0, 0]

  for i in range(n):
    face = random.randint(1,6)
    if face == 1:
      frequencies[0] += 1
    elif face == 2:
      frequencies[1] += 1
    elif face == 3:
      frequencies[2] += 1
    elif face == 4:
      frequencies[3] += 1
    elif face == 5:
      frequencies[4] += 1
    elif face == 6:
      frequencies[5] += 1

  print(f'Face {"Frequency":>13}')
  for i in range(6):
    print(f'{i+1:>4}{frequencies[i]:>13}')

# Call Function
roll(120)

"""---

__Example__:  Simulate flipping a coin 20 times.
"""

import random 

for i in range(20):
  print('H' if random.randint(0,1) == 0 else 'T', end=' ')

"""## Reproducibility

Reproducibility is important to scientific results.  It is also crucial to __debugging__ code.  

Computers actually only generate __psuedorandom__ numbers (seemingling random, for most intent and purposes, but actually deterministic). 

But each call, the psuedorandom generator  __seeds__ the algorithm and the results are different.  If we wish to ensure reproducibility, we can manually set the seed value.
"""

random.seed(345)
roll(10)



"""# Case Study: Craps

The rules for the game of "craps":
1. Roll a pair of six-sided dice.
 - if 7 or 11 $\rightarrow$ W
 - if 2, 3 or 12 $\rightarrow$ L
 - if 4,5,6,8,9, or 10, record as "point"
2. Roll pair again
  - if 7 $\rightarrow$ L
  - if point $\rightarrow$ W
  - else record point.
3. Goto 2.

Write a program to simulate "craps".
"""

"""Simulate Craps"""
# Quinlan, J
# 2021-09-25 

import random

# Support Functions
def roll_dice():
  return (random.randint(1,6),random.randint(1,6))

def show_roll(dice):
  die1, die2 = dice
  print(f'Player roll {die1} + {die2} = {sum(dice)}')

def game_status(dice, point):
  if sum(dice) == 7:
    return (True,'L')
  elif sum(dice) == point:
    return (True,'W')
  else:
    return (False,'Continue')

# First Roll
dice = roll_dice()
sum_of_dice = sum(dice)
point = sum_of_dice
show_roll(dice)
 
if sum_of_dice in (7,11):
  game_over = game_status((1,1),2)
elif sum_of_dice in (2,3,12):
  game_over = game_status((1,6),0)
else:
  game_over = (False,'Continue')

# Continue Rolling
while not game_over[0]:
  x = input('Enter X to exit: ')
  if x == 'X':
    break
  dice = roll_dice()
  show_roll(dice)
  game_over = game_status(dice, point)
  point = sum(dice)
  print(game_over)

"""---

# Python Standard Library

There are plenty of prebuilt modules in the standard library.  Some popular modules in the standard library are listed in the table below.  See also [1, p. 132].

| Module      |  Description   |
|-------------|----------------|
| ```math```  | Comman math constants and operations |
| ```random```| Psuedorandom number generators|
|```statistics``` | Statistical functions |
|```sqlite3``` | SQL functions |

### ```math``` Module
"""

import math

x = 4.762

math.ceil(x)
math.floor(x)

math.sin(x)
math.cos(x)
math.tan(x)

math.exp(x)
math.log(x)
math.log10(x)

math.pow(x,2)
math.sqrt(x)

math.fabs(x)
math.fmod(17,4)

math.pi

import math
math.cos(0)

del math

from math import cos
cos(0)

import math as m

m.sin(0)

"""There are many other functions included in the ```math``` module."""



"""## `import`: A closer look

We can import the entire library
```
import math
```

Or only parts of a library, in particular, certain functions

```
from math import ceil
```

It is possible to import multiple functions by a comma-separated list.
```
from math import ceil, floor
```

In the first case, i.e., `import library`, must use fully qualified name with functions.  For example,
"""

import math
sqrt(5)
math.ceil(sqrt(5))

"""In the second case where only certain functions are included, a call to the function works."""

from math import ceil

ceil(5)

"""## Wildcard Imports
 __Advoid__ using the wildcard to import "everything".  Loads everything into the current scope. 
```
from math import *
```

## Aliasing the namespace
"""

import numpy as np

np.zeros((5,2), dtype=int)

# Data Science Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt