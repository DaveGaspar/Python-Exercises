import re

word = input("Enter the word: ")
word = re.sub(r'[^a-zA-Z0-9]', '', word.lower())
rev = word[::-1]

if word == rev:
    print("The entered word is a palindrome")
else:
    print("The entered word isn't a palindrome")
