def fact(n):
    if not isinstance(n, int) or n < 0:
        raise TypeError("Factorial is only defined for non-negative integers")
    elif n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

print(fact(125))
