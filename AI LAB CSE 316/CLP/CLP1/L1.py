numberRange = int(input("Enter the range of numbers: "))
sum_odd = 0 
sum_even = 0

for i in range (numberRange+1):
    if i%2 == 0:
        sum_even += i
    else:
        sum_odd += i
        
print("Sum of Odd numbers (1-10): "+ str(sum_odd))
print("Sum of Even numbers (1-10): "+ str(sum_even))