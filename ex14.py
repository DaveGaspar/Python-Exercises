def count_of_items(items):
    if (type(items) != list):
        print("Error, expected a list!")
        return None
    count = 0
    for item in items:
        count += 1
    return (count)

arr = input("Enter items separated by space: ").split()
print("Count of items: ", count_of_items(arr))
