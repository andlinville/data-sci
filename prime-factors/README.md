Prime Factors
=============

Code related to the admissions problem

### Problem

The prime factors of 13195 are 5, 7, 13 and 29.  What is the largest prime factor of the number 600851475143?

### First Pass

This was the first algorithm that came to mind. I tried a couple optimizations (looping through smaller sets of numbers by, say, skipping even numbers, etc.), but nothing would get the code to run quickly enough to solve the problem.

### Second Pass

After racking my brain for long-forgotten middle school math lessons and reading up on factor trees, I came to this solution. The problem lends itself naturally to recursion--find the lowest factor, which must be prime, and then call the same function on the other half of the resulting factor pair.

### Solution

The output of my second pass:

```python
a = 13195
print('Example problem:')
print(get_all_prime_factors(a, []))
print()

b = 600851475143
factors = get_all_prime_factors(b, [])
print('Real problem:')
print(factors)
print(max(factors))

## Example problem:
## [5, 7, 13, 29]
##
## Real problem:
## [71, 839, 1471, 6857]
## 6857