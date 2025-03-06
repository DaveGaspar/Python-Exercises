while True:
    try:
        n = int(input("Enter a number: "))
        if n == 0:
            break
        elif n % 2 == 0:
            print("Entered number is even!")
        else:
            print("Entered number is odd!")
    except ValueError:
        print("Invalid input!")
