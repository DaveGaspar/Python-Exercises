string = input("Enter a string: ")
if not string.strip():
    print("Invalid input! Please enter a non-empty string.")
    exit()

print(string[::-1]) 
