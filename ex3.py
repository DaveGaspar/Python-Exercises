while(True):
    try:
        oper = int(input("Choose an operation:\n 1 (+)\n 2 (-)\n 3 (*)\n 4 (/)\n 5 (exit)\n\n"))
        if (oper == 5):
            break
        arg1 = int(input("Enter the 1st argument: "))
        arg2 = int(input("Enter the 2nd argument: "))

        match oper:
            case 1:
                print(arg1 + arg2, "\n")
            case 2:
                print(arg1 - arg2, "\n")
            case 3:
                print(arg1 * arg2, "\n")
            case 4:
                if (arg2 == 0):
                    print("Can't divide on zero!\n")
                else:
                    print(arg1 / arg2, "\n")
            case 5:
                break
    except:
        print("Invalid input!\n")
