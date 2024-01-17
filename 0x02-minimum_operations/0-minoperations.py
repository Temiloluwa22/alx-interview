#!/usr/bin/python3
def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    if n > 1:
        operations += n
    
    return operations

# Example usage
n1 = 4
print("Min # of operations to reach {} char: {}".format(n1, minOperations(n1)))

n2 = 12
print("Min # of operations to reach {} char: {}".format(n2, minOperations(n2)))
