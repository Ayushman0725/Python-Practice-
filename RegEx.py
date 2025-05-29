'''import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)'''

'''import re

txt = "The rain in Spain"
x = re.findall("i", txt)
print(x)'''

'''import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
'''
'''import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)'''

'''import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
'''

'''import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)'''

'''import re

txt = "The rain in Spain"
x = re.search("ra", txt)
print(x) #this will print an object
'''

'''import re

txt = "The Rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())'''

import re

'''txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)'''

import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)


