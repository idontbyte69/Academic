n = int(input("Enter a number: "))

factorial = 1
if n < 0:
    print("Please give a positive number")
elif n == 0:
    print("The factorial of 0 is always 1")
else:
    for i in range(1, n+1):
        factorial *= i
    print(f"Factorial of {n} is: {factorial}")
    
        