# fib.py

#
# Prints Fibonacci numbers using a for-loop
#

a, b = 1, 1
for i in range(10):
    print(a)
    a, b = b, a + b
