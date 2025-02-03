sum=0

for i in range (50, 100):
    if i%3 == 0 and i%5 != 0:
        sum += i        

print("Sum of all numbers between 50 - 1000 which are divisible by 3 and not divisible by 5: ", sum) 
    