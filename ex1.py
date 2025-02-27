arr = []

while(True):
    n = int(input("Enter 1 or 2: "))
    if (n == 1):
        arr.append(int(input("Enter a number: ")))
    elif (n == 2):
        break
    else:
        continue

print("Sum: ", sum(arr))
