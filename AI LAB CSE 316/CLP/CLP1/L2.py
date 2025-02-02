numbers = input("Enter numbers: ").split()
numbers = [int(n) for n in numbers]

if numbers:
    smallest = numbers[0]
    for n in numbers[1:]:
        if n < smallest:
            smallest = n 
    print("The smallest number is: ", smallest)
else:
    print("invalid")
