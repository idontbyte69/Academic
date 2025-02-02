n = int(input("Enter a number: "))

x, y = 0, 1

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print(f"Fibonacci Series up to {n}: ")
    print(x)
else:
    print(f"Fibonacci Series up to {n}: ")
    print(x, end = ", ")
    print(y, end = ", ")
    for i in range (2, n):
        z = x + y
        print(z, end = ", ")
        x, y = y, z 
    
    