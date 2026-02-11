# is_prime.py

#
# This is a boolean function that tests if a number is prime.
#
def is_prime(n):
    # TODO: implement this function
    pass

def is_prime_demo():
    for i in range(21):
        if is_prime(i):
            print(f'{i} is prime')
        else:
            print(i)

def num_primes(n):
    """Returns the number of primes less than, or equal to, n.
    """
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count

def num_primes_demo():
    N = 10000
    print(f'# of primes less than {N}: {num_primes(N)}')

is_prime_demo()
# num_primes_demo()
