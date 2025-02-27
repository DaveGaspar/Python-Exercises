def fact(n):
    if (type(n) != int or n < 0):
        print("Invalid input!\n")
        return None
    elif (n == 0 or n == 1):
        return (1)
    return (n * fact(n - 1))

print(fact(5))
