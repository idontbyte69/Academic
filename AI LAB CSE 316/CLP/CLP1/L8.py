def sumOfNumbers (numbers):
    sum = 0
    for i in range(len(numbers)+1):
        sum += i
    print(f"Sum = {sum}")
    
numbers = input("Enter numbers: ").split()
numbers = [int(n) for n in numbers]

sumOfNumbers(numbers)

