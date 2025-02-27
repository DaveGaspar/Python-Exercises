n = int(input("Enter the lenght of list: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element number {i}: ")))

mx = None
sec = None

for i in arr:
    if not mx or i > mx:
        if mx:
            sec = mx
        mx = i

print("Second mx: ", sec)
