import random

count = 0
n = random.randrange(1, 10, 1)

while(True):
    count += 1
    guess = None
    while (guess == None):
        try:
            guess = int(input("Guess a number: "))
            break
        except:
            print("Invalid input!")
    if (guess == n):
        print(f"Correct!!! It took {count} tries")
        break
    elif (guess > n):
        print("Too high")
    else:
        print("Too low")
