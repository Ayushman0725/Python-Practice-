'''def my_function():
    print("Hello from my function")

my_function()'''

# Arguments:
'''def my_function(fname):
  print(fname + " Kumar")

my_function("Aryan")
my_function("Ayushman")
my_function("Sahil")'''

'''def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")'''

'''def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")'''

'''def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")'''

'''def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")'''

'''def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)'''

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
