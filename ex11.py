vowels = {'a', 'e', 'i', 'o', 'u'}
count_of_vowels = 0

word = input("Enter a string: ").lower()
for i in word:
    if i in vowels:
        count_of_vowels += 1

print("Count: ", count_of_vowels)
