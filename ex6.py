word = input("Enter the word: ")
rev = word[::-1]

if (word == rev):
    print("The entered word is a palindrome")
else:
    print("The entered word isn't a palindrome")
