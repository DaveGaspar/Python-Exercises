vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
count = 0

word = input("Enter a string: ")
for i in word:
    if i in vowels:
        count += 1

print("Count: ", count)
