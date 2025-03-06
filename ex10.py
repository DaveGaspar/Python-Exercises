def fibo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo (n - 2)

try:  
    n = int(input("Enter a number: "))  
    if n < 0:  
        print("Invalid input!")  
        exit()  
except ValueError:  
    print("Invalid input! Please enter an integer.")  
    exit()  

arr = []
for i in range(0, n + 1):
    arr.append(fibo(i))

print(arr)
