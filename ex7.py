try:
    n = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter an integer.")
    exit()
for i in range(1,11):
    print(f"{n} * {i} = {n * i}")
