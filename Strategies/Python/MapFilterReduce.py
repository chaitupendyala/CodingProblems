print('''
**************************************************
*********************MAP**************************
**************************************************
''')
'''
If want to find the area of a number of radii
'''
# Conventional Way:
import math
def area(radius):
    return math.pi * (radius ** 2)

radii = [2,5,7.1,0.3,10]
radii = [area(radius) for radius in radii]
print(radii)

# Using Map:
radii = [2,5,7.1,0.3,10]
radii = list(map(area, radii))
print(radii) # [12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793]

'''
Convert temp from C to F
'''
temps = [("Berlin", 29), ("Los Angeles", 33), ("New York", 30), ("Tokyo", 10), ("Mumbai", 50)]
# C to F = (9/5*C) + 32
c_to_f = lambda data: (data[0], (9/5*data[1]) + 32)
print(list(map(c_to_f, temps))) # [('Berlin', 84.2), ('Los Angeles', 91.4), ('New York', 86.0), ('Tokyo', 50.0), ('Mumbai', 122.0)]

print('''
**************************************************
*********************FILTER***********************
**************************************************
''')
'''
Remove certail data from a list etc.
'''
data = [1,2,3,4,5,6,7]
print(list(filter(lambda x: x>4, data))) # [5, 6, 7]

'''
Remove empty countries
'''
countries = ['', 'India', 'USA', 'Argentina', 'China', 'Japan', '', 'Nepal', '']
print(list(filter(None, countries))) # ['India', 'USA', 'Argentina', 'China', 'Japan', 'Nepal']

data = ["", 0, 0.0, 0j, [], (), {}, False, None]
print(list(filter(None, data))) # []

print('''
**************************************************
*********************REDUCE***********************
**************************************************
''')
from functools import reduce
numbers = [1,2,3,4,5,6,7,8,9,10]
print(reduce(lambda x,y: x*y, numbers)) # 3628800