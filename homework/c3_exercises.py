# - Introduction to Programming with Python
# - Chapter 3 Exercises on REPETITION statements
# - DSC-225 Fall 2021
# - Quinlan, J


# 3.1 (Validating User Input)
"""
Modify the script of Fig. 3.3 to validate its inputs.  For any input, if the 
value entered is other than 1 or 2, keep looping until the user enters a correct
value.  Use one counter to keep track of the number of attempts, then 
calculate the number of failures after all the user's inputs have been received.
"""

# fig 3.3
'''Nested control statements to analyze exam results'''

# initialize variables
passes = 0

for student in range(10):
  flag = True
  while flag:
    result = int(input('Enter result (1 = pass, 2 = fail): '))
    if result == 1:
      passes += 1
      flag = False
    elif result != 2:
      print('Incorrect input.\n')
    else:
      flag = False

# Print results
print('Number of students passing = ',passes)
print('Number of students failing = ', 10 - passes)

# \{end} 




# 3.2 What's wrong with the code?
'''
ANS: Nothing really.  Typically use two lines:
a = 7
b = 7
'''

a = b = 7
print('a = ',a,'\nb = ', b)

# 3.3 (What does this code do?)
"""
Run the following code.  See what it does.
"""

for row in range(10):
  for column in range(10):
    print('<' if row % 2 ==1 else '>', end='')  # end='' prevents a carriage return
  print() # newline

# The code prints 10 '>' for odd rows and 10 '<' if row is even.
# print() puts new line.

# \{end} 




# 3.4 (Fill the missing code)
"""
for ***:
  for ***:
    print('@')
  print()

Replace code to print:
@@@@@@@
@@@@@@@
"""

for row in range(2):
    for column in range(7):
        print('@',end='')
    print()

# \{end} 






# 3.5 (if...else)
"""
Reimplement the script of Fig. 2.1 using three if...else statements
rather than six if statements.  Hint: think of == and != as opposite
tests.
"""

# \{end} 




# 3.6 (Turing Test - Chatbot)
"""
Alan Turing developed a simple test to determine whether machines could
exhibit intelligent behavior.  Can you determine if its a chatbot or human?
If a user can't tell if a response is a human or a computer, then it is reasonable
to say the computer is exhibiting intelligence.  

Create a script that plays the part of the independent computer, giving the user
a simple medical diagnosis.  The script will prompt the user with 'What is your problem?'
Then prompt the user again with 'Have you had the problem before (yes or no)?'
If yes, print 'You have it again'.  If no, then 'You have it now.'
"""

input('What is your problem? ')
yes_no = input('Have you had this before (yes or no)? ')

if yes_no == 'yes':
  print('You have it again.')
elif yes_no == 'no':
  print('Well, you have it now!')

# \{end} 




# 3.7 (Table of SQuares and Cubes)
"""
Use a for loop and the f-string capabilities to produce the following table
with numbers aligned right.

number  square  cube
    0        0      0
    1        1      1
    2        4      8
    3        9     27
    4       16     64
    5       25    125
"""

print(f'number\t', 'square\t\t','cube')
for i in range(6):
  print(f'{i:>6} \t {i*i:>6} \t {i*i*i:>4}')

# \{end} 








# 3.8 (Arthmetic: smallest and largest)
"""
Reimplement code from Exercise 2.10 that computes and displays sum, average, product, 
smallest and largest value using a loop that inputs four values.  
"""

# \{end} 


# 3.9 (Separating the Digits in an Integer)
"""
In #2.11, we separated a five-digit integer into its individual digits and 
displayed them.  Reimplement to use a loop that in each iteration "picks off"
one digit (left to right) using the // and % operators, then displays that digit.
"""

# \{end} 


# 3.10 (7% investment return)
"""
Reimplement Exercise 2.12 to use a loop that calculates and displays the amount
of money you will have each year at the ends of years 1 through 30.  
"""

p = 100
for n in range(31):
  print(f'{n}\t{p*(1.07)**n:.2f}')

# \{end} 




# 3.11 (Miles per gallon)
"""
Develop a sentinel-controlled-repetition script that prompts the users
for miles driven and gallons used for each tank.  The script should calculate
and display the miles per gallon obtained for each tank. Then, calculate and 
display the miles per gallon obtained for all tankfuls (total miles / total gallons used).

The sentinel value is -1.  
"""

# Initialize variables
mpg = 0
total_miles = 0
total_gallons = 0

gallons = float(input('Enter the gallons used (-1 to end): '))
while gallons != -1:
  miles = float(input('Enter the miles driven: '))
  print(f'The miles/gallon for this tank was {miles/gallons:.2f}')
  total_gallons += gallons
  total_miles += miles
  gallons = float(input('Enter the gallons used (-1 to end): '))

mpg = total_miles / total_gallons
print(f'The overall average miles/gallon was {mpg:.2f}')

# \{end} 





# 3.12 (Palindromes)
"""
A palindrome is a number, word, or text phrase that is the same forwards and 
backwards.  For example, 12321, Hannah, 555555, 345543, 11611.  Write code 
that reads in a five-digit integer and determines whether its a palindrome.  
Hint: use \\ and % to separate the numbers into its digits.  
"""

# assume user enters 5-digit integer, i.e., no validation needed.
# word = int(input('Enter a 5-digit number: '))

word = 13821
# for i in range(2):
first = word // 10000
last = word-10*(word//10)

if first != last:
  print('Not Palidrome')
else:
  second = (word - 10000*first)//1000
  fourth = (word - 100*(word//100))//10
  if second != fourth:
    print('Not palidrome')  
  else:  
    print('Palindrome')

# \{end} 




# 3.13 (Factorials)
"""
Factorial calculationsn are common in probability.  the factorial of a 
nonnegative integer n is written n! and is defined as:
\[
    n! = n \cdot (n-1) \cdot (n-2) \cdots 2 \cdot 1, for n > 0
\]
and where 0! = 1.
Write a script to calculate n!
"""

n = 10
nfactorial = 1
for i in range(n,1,-1):
  nfactorial *= i
print(nfactorial)

# -- \{end} 



# 3.14 (Approximate \pi)
"""
Write code to approximate the value of pi from the following infinite series.
\[ \pi = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ... + (-1)^k*4/(2*k+1) + ... \]
How many terms are needed to get 3.14? 3.141? 3.1415? 3.14159?
"""

n = 10000000 # number of terms
pi = 0
for i in range(n):
  sign = (-1)**(i % 2)
  pi += sign*(4/(2*i+1))
print(pi)

# \{end} 



# 3.15 (Approximate e)
"""
Approximate e using Taylor series
\[
    e = 1 + \frac{1}{1!} + \frac{1}{2!} + \dots 
\]
"""

n = 20 # number of terms
e = 0
for i in range(1,n):
  denom = 1
  
  for j in range(1,i):
    denom *= j

  e += 1/denom

print(e)

# \{end} 




# 3.16 (Nested Control Statements)
"""
Use a loop to find the two largest values of 10 entered numbers.
"""

biggest1 = 0
biggest2 = 0

for i in range(10):
  x = int(input('Enter integer = '))
  if x > biggest1:
    biggest2 = biggest1
    biggest1 = x
  elif x > biggest2:
    biggest2 = x
    
print(biggest1,biggest2)

# \{end} 




# 3.17 (Nested Loops)
"""
Write a script that displays the following triangle patterns (e.g.)
* 
**
***
****
*****
one below the other with a blank line separating each.  See page 114
"""

#(a)
stars = ''
for i in range(10):
  stars=stars+'*'
  print(stars)

print('\n')

stars = '**********'
for i in range(10,0,-1):
  print(stars[1:i])

print('\n')

stars = '**********'
spaces ='          '
for i in range(10,0,-1):
  print(spaces[0:10- i]+stars[1:i])

# \{end} 



# 3.18 (Nested Loops)
"""

"""
for i in range(10):
  print('*'.rjust(i, ' '))

# \{end} 



# 3.19 (Brute-force Pythagorean Triples)
"""
A right triangle can have sides that are all integers.  The set of three integer
values for the sides of a right triangle is called  a Pythagorean tripe.  
These three sides must satisfy the relationship that the sum of the squares of 
the two sides is equal to the square of the hypotenuse.  Find ALL Pythagorean
triples less than N.  Some problems have no known algorithm other than brute-force.
"""

N = 20
for a in range(1,N):
  for b in range(1,N):
    for c in range(1,N):
      if a**2+b**2 == c**2:
        print(a,b,c)

# \{end} 



# 3.20 (Binary to Decimal Conversion)
"""
Input a binary and convert to decimal.
"""

x = input('Enter binary number: ')
# x = '1001'
n=len(x)


y = 0
for i in range(n-1,-1,-1):
  y = y + 2**i*int(x[i])

print(y)

# \{end} 




# 3.21 (Calculate change with fewest number of coins)
"""
Suppose an item costs $1.00 or less and customer pays with $1.00.  
Write a script to input cost of item and calculate the change.  Use 
fewest coins.
"""

cost = 25 # in cents
change = 100 - cost
print(change)

quarters = change//25
change = change - 25*quarters

dimes = change // 10
change = change - 10*dimes

nickels = change // 5
pennies = change -  5*nickels


print(quarters, dimes, nickels, pennies)

# \{end} 




# 3.22 (Optional else clause of a loop)
"""
The `while` and `for` statements each have an optional else clause. In a while
statement, the else clause executes when the condition becomes False.  In a for
statement, the else clause executes when there are no more itmes to process.  If 
you break out of a while or for that has an else, the else part does NOT execute.
Run the following code.
"""

for i in range(2):
  value = int(input('Enter (-1) to break: '))
  print('You entered', value)

  if value == -1:
    break
else:
  print('Loop terminated without executing the break. This is the ELSE clause')

# \{end} 




# 3.23
"""

"""

# \{end} 


# 3.24 (Prospector)
"""
The prospector tool run several popular static code analysis tools to check 
your Python code for common errors and to help improve your code.

prospector --strictness veryhigh --doc-warnings
"""

# 3.25 (Prospector to analyze open-source code on github)
"""
Download a python project from GitHub and navigate to the directory and run the
command:

prospector --strictness veryhigh --doc-warnings
"""

# 3.26 (Anscombe's Quartet)
"""
In the data science case studied, importance of "getting to know your data" 
is emphasized.  The basic descriptive statistics seen help you know your data.
One caution is that different data setscan have identical or nearly identical descriptive statistics
and yet the data can be significantly different.  For example, research Anscombe's Quartet.  You 
should find four datasets and the associated visualizations.  Its the visualizations
that convince you the datasets are quite different.  In a later exercise you'll 
create the visualizations.  
"""

# \{end} 


# 3.27 (World Population)
"""
Write a script that calculates world population growth for next 100 years.
Print results in 3 column table with Col 1 = 1:100, Col 2 = Pop at end of year, 
and Col 3 = difference in population from the last year.  Determine when population
doubles and quadruples.
"""

P0 = 7886525974  # Current World Pop ~ 7.8 billion
rate = 0.0112    # growth rate = 1.12%

P1 = P0
for i in range(1,101):
  P = P1*(1+rate)
  print(i,round(P),round(P-P1)) 
  P1 = P

# \{end} 


# 3.28 (Mean, median, and mode)
"""
Calculate the mean, median, and mode of the values:
9, 11, 22, 34, 17, 22, 34, 22, and 40.  What is the problem if
there is another 34?

See Section 3.17 p. 109
"""

values = [9, 11, 17, 17, 21, 34, 17, 22, 34, 32, 40, 50, 17]

# using statistic module
import statistics

print(statistics.mean(values))
print(statistics.median(values))
print(statistics.mode(values))

# 'old fashion' method...need to sort list
sorted_values = sorted(values)
mean = 0
median = 0

print(sorted_values)


# Mean
for v in values:
  mean += v
mean = mean/len(values)
print('Mean = ', mean)


# Median
middle = len(values)//2
if len(values) % 2 == 1:
  print('Median = ', sorted_values[middle])
else:
  print('Median = ', (sorted_values[middle-1]+sorted_values[middle])/2)


# Mode (needs work)
mode = sorted_values[0] # initialize to the first value
count = 0
maxcount = 0

for v in sorted_values:
  if mode == v:
    count +=1
  else:
    count = 1
  
  if count >= maxcount:
    maxcount = count
    mode = v   

print('Mode = ', mode)

# ------------------------------- #


# 3.29 (Problem with the Median)
"""

"""

# \{end} 


# 3.30 (DS: Outliers)
"""
In statistics, outliers are values out of the ordinary and possibly way out of
the ordinary.  Sometimes, outliers are simply bad data.  In the data science
case studies, we will see that outliners can distory results.  Which of the three 
measures of central tendency we discussed -- mean, median, and mode -- is most
effected by outliers?  Why?  Which of these measures are not affected or least
affected? Why?
"""

# \{end} 


# 3.31 (DS: Categorical Data)
"""
Mean, median, and mode work well with numerical values.  You can use them in 
calculations and arrange them in meaningful order.  Categorical values are 
descriptive names like Boxer, Poodle, Collie, Beagle, Bulldog, and Chihuahua.
Normally, you don't use these in calculations nor associate an order with them.
Which if any of the descriptive statiscs are appropriate for categorical data?
"""

# misc. test code

# Grades
count = 0
total = 0

grade = int(input('Enter grade, (-1 to end): '))
while grade != -1:
  total += grade
  count += 1
  grade = int(input('Enter grade, (-1 to end): '))


print(total)
print(count)

average = total/count
if average != -1:
  print(f'Class average is {average:.2f}')