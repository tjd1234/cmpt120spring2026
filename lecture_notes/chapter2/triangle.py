# triangle.py

#
# This program calculates the hypotenuse of a right triangle
# given the lengths of the two sides:
#
#      |\
#      | \
#      |  \
#    a |   \  hypotenuse = sqrt(a ** 2 + b ** 2)
#      |    \
#      |     \
#      +------+
#         b
#

import math

# get the sides of the triangle
a = 3
b = 4

# calculate the hypotenuse of the triangle using the Pythagorean theorem
hypotenuse = math.sqrt(a ** 2 + b ** 2)

# print the results
print(hypotenuse)
