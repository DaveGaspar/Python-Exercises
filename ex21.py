def armstrong(n):
    m = n
    digits = []
    while (m > 1):
        digits.append(int(m % 10))
        m /= 10

    sum = 0
    for digit in digits:
        sum += digit ** len(digits)

    return (n == sum)


n = int(input("Enter a number: "))

print('The number is Armstrong number' if armstrong(n) else 'The number is not Armstrong number')
