n = int(input("Enter the lenght of list: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element number {i}: ")))

print("Sum: ", sum(arr))
