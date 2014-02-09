# python 3.3

def get_all_prime_factors(x, factors):

    i = 2
    while x % i != 0 and i**2 <= x:
        i += 1
    if i ** 2 > x:
        factors.append(x)
        return factors
    else:
        factors.append(i)
        x = int(x / i)
        return get_all_prime_factors(x, factors)
    
if __name__ == '__main__':
    a = 13195
    print('Example problem:')
    print(get_all_prime_factors(a, []))
    print()

    b = 600851475143
    factors = get_all_prime_factors(b, [])
    print('Real problem:')
    print(factors)
    print(max(factors))
    
    
