import random

count = 0
n = random.randint(1, 10)

while True:
    while True:
        try:
            guess = int(input("Guess a number: "))
            count += 1
            break
        except ValueError:
            print("Invalid input!")
    if guess == n:
        print(f"Correct!!! It took {count} tries")
        break
    elif guess > n:
        print("Too high")
    else:
        print("Too low")
