def largestNum(x,y):
    if x<y:
        print(f"{y} is the largest number.")
    elif x>y:
        print(f"{x} is the largest number")
        
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

largestNum(num1, num2)