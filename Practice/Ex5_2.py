largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            number = int(num)
        except:
            print("Invalid input")

    if largest == None:
        largest = number
    elif number > largest:
        largest = number

    if smallest == None:
        smallest = number
    elif number < smallest:
        smallest = number

print("Maximum is", largest)
print("Minimum is", smallest)
