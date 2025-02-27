while(True):
    n = None
    try:
        n = int(input("Enter a number: "))
        if (n == 0):
            break
        elif (n % 2 == 0):
            print("Entered number is even!\n")
        else:
            print("Entered number is odd!\n")
    except:
        print("Invalid input!\n")
