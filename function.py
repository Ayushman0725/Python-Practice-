'''def my_function():
    print("Hello ")

my_function()
my_function()'''


'''def fahrenheit_to_celcuis(fahrenheit):
    return (fahrenheit - 32) * 5/9

print(fahrenheit_to_celcuis(77))
print(fahrenheit_to_celcuis(100))'''

# Return Values

'''def get_greeting():
    return "Hello from a function"
message = get_greeting()
print(get_greeting())'''

'''def get_greeting():
    return "Hello from a function"

print(get_greeting()) '''

#  Arguments

'''def my_function(fname):
    print(fname +  " Refsnes")


my_function("Email, mobile")
my_function("Tobias")
my_function("Linus") '''

'''def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")  '''

# Default Parameter

'''def my_function(name = "friend"):
    print("hello" , name)

my_function()
my_function("Aaryan") '''

# Keywords Arguments

'''def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy") '''

# Positional Arguments

'''def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy") '''


# Mixing Positional & Keyword Arguments

''''def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)'''


# Passing Different DataTypes

'''def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits) '''

'''def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person) '''

# Return Values

'''def my_function(x, y):
  return (x - y)


result = my_function(5, 3)
print(result) '''

# Return Different Data Types

'''def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2]) '''

'''def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)'''

#Passing Only Arguments

'''def my_function(name, /):
  print("Hello",name)

my_function("Emil")'''

'''def my_function(name):
  print("Hello", name)

my_function(name = "Emil") '''

# Combining Positional-Only and Keyword-Only

'''def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10,c = 15, d = 20)
print(result)'''


# Arbitrary Arguments - *args

'''def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") '''

'''def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus") '''


'''def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus") '''

'''def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))
print(my_function(1,2,3,4,5,6,7,8,9,10)) '''

'''def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))  '''

'''def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())
'''
#Decorators
# A basic decorator that uppercases the return value of the decorated function.

'''def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello Aaryan"

print(myfunction()) '''

#Using the @changecase decorator on two functions:

'''def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Aaryan "

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction()) '''

#Functions with arguments can also be decorated:

'''def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John")) '''

# Preserving Function Metadata
'''def myfunction():
  return "Have a great day!"

print(myfunction.__name__) '''

'''def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__) '''

# Lambda Function
'''x = lambda a,b :  a * b
print(x(5,2))
print(x(5,3))
print(x(5,4))'''

'''def myfunc(n):
    return lambda a : a * n
x = myfunc(4)
print(x(11)) '''


'''numbers = [1,2,3,4,5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)'''

'''students = [("Aryan", 22), ("Tobias",24), ("Ashutosh", 13)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students) '''

'''numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)'''

# Recursion

#A simple recursive function that counts down from 5:

'''def countdown(n):
    
    if n <= 0:
        print("Done")

    else:
        print(n)
        countdown(n - 1)

countdown(4)'''

#Identifying base case and recursive case:

'''def factorial(n):
    #base case

  if n == 0 or n == 1:
    return 1
  
  #recursive case
  else:
    return n * factorial(n - 1)
  
print(factorial(5))'''

#Find the 7th number in the Fibonacci sequence:

'''def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(9)) '''

#calculate the sum of all elements in a list

'''def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    
    else:
        return numbers[0] + sum_list(numbers[1:])
    

my_list = [1,2,3,4,5]
print(sum_list(my_list)) '''

#Find the maximum value in a list:

'''def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))'''

'''import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit()) '''

# Python Generators


'''def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6

for value in my_generator():
    print(value)'''

'''def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)'''





