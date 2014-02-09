# python 3.3
import time

def is_prime(x):
    if x%2 == 0:
        return False
    for i in range(3, int(x/2)+1, 2):
        if x % i == 0:
            return False
    
    return True


def is_factor(x, y):
    return y % x == 0

def get_largest_prime_factor(x):
    factors = []
    time1 = time.time()
    if int(x/2)%2 == 0:
        start = int(x/2) - 1
    else:
        start = int(x/2)
    for i in range(start, 1, -2):
        if is_factor(i, x):
            if is_prime(i):
                time2 = time.time()
                print('This function took ' + str(time2 - time1))
                return i
            
    time2 = time.time()
    print('This function took ' + str(time2 - time1))
    if not x%2 == 0:
        return x
    else:
        return 'Something went wrong'
