arr = []
print("1 to add numbers\n2 to display sum and exit\n3 to display sum\n\n")

while(True):
    try:
        n = int(input("Enter 1 | 2 | 3: "))
        if (n == 1):
            arr.append(int(input("Enter a number: ")))
            print('Number added succesfully!')
        elif (n == 2):
            break
        elif (n == 3):
            print("Total_sum: ", sum(arr))
    except ValueError:
        print("Invalid input")

print("Total_sum: ", sum(arr))
